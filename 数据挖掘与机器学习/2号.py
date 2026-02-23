import itertools
import time
import numpy as np
import pandas as pd
import requests
from collections import Counter


# 第一部分：暴力破解法实现
class BruteForceFIM:
    def __init__(self, transactions, items):
        self.transactions = transactions
        self.items = sorted(items)  # 排序以便确定性
        self.n = len(items)         # 商品总数
        self.m = len(transactions)  # 交易总数

    def generate_all_itemsets(self):
        """生成所有可能的非空项集 (从1项集到最大项集)"""
        all_itemsets = []
        # 生成从1到n项集的所有组合
        for r in range(1, self.n + 1):  # 从1项集到n项集
            for itemset in itertools.combinations(self.items, r):
                itemset=set(itemset)
                all_itemsets.append(set(itemset))  # 将每个项集转为集合
                print(itemset)
        return all_itemsets

    def calculate_support(self, itemset):
        """计算项集支持度"""
        # 计算该项集在所有交易中出现的次数，并除以交易总数
        support_count = sum(1 for transaction in self.transactions if itemset.issubset(set(transaction)))
        return support_count / self.m


    def find_frequent_itemsets(self, min_support):
        """根据最小支持度筛选频繁项集"""
        frequent_itemsets = []
        all_itemsets = self.generate_all_itemsets()  # 生成所有项集

        # 遍历所有项集，计算支持度
        for itemset in all_itemsets:
            support = self.calculate_support(itemset)
            if support >= min_support:  # 如果支持度大于等于最小支持度，则为频繁项集
                frequent_itemsets.append((itemset, support))

        return frequent_itemsets

# 第二部分：数据集处理
class groceriesDataManager:
    """加载和预处理Groceries数据集"""

    def __init__(self):
        self.datasets = {}

    def download_groceries(self):
        """下载Groceries数据集"""
        try:
            url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/groceries.csv"
            response = requests.get(url)
            response.raise_for_status()

            # 解析CSV数据
            transactions = []
            for line in response.text.strip().split('\n'):
                items = line.split(',')
                transactions.append([item.strip() for item in items if item.strip()])

            print(f"成功加载 Groceries 数据集: {len(transactions)} 笔交易")
            return transactions
        except Exception as e:
            print(f"下载Groceries数据集失败: {e}")
            # 返回一个示例数据集作为后备
            return [
                ['牛奶', '面包', '黄油'],
                ['啤酒', '面包'],
                ['牛奶', '面包', '啤酒'],
                ['牛奶', '面包'],
                ['面包', '黄油'],
                ['牛奶', '啤酒'],
                ['面包', '啤酒'],
                ['牛奶', '面包', '啤酒', '黄油'],
                ['牛奶', '面包', '啤酒']
            ]

    def analyze_dataset(self, transactions):
        """分析数据集特性"""
        all_items = set(item for trans in transactions for item in trans)
        total_positions = len(transactions) * len(all_items)
        actual_items = sum(len(trans) for trans in transactions)

        stats = {
            'n_transactions': len(transactions),
            'n_items': len(all_items),
            'avg_transaction_size': np.mean([len(trans) for trans in transactions]),
            'sparsity': 1 - (actual_items / total_positions) if total_positions > 0 else 0,
            'max_transaction_size': max(len(trans) for trans in transactions),
            'min_transaction_size': min(len(trans) for trans in transactions)
        }
        return stats

    def preprocess_groceries(self, transactions):
        """只保留频率最高的20个商品，并取前100条交易"""
        # 统计每个商品的出现次数
        item_counts = Counter(item for transaction in transactions for item in transaction)
        top_20_items = [item for item, _ in item_counts.most_common(20)]

        # 过滤交易数据，只保留频率最高的20个商品
        filtered_transactions = [
            [item for item in transaction if item in top_20_items]
            for transaction in transactions[:100]
        ]

        return filtered_transactions, top_20_items


class SyntheticDatasetGenerator:
    """生成更接近真实数据的合成数据集"""

    def __init__(self, groceries_transactions, seed=42):
        self.seed = seed
        np.random.seed(seed)
        self.groceries_transactions = groceries_transactions

    def generate_dataset(self, config):
        """
        生成合成数据集
        config = {
            'n_transactions': 100,    # 交易数量
            'n_items': 20,            # 商品种类
            'avg_transaction_size': 8,# 平均交易大小
            'correlation_strength': 0.6  # 商品相关性
        }
        """
        # 获取数据中最常见的商品
        item_counts = Counter(item for transaction in self.groceries_transactions for item in transaction)
        top_items = [item for item, _ in item_counts.most_common(config['n_items'])]  # 取频率最高的商品

        # 生成合成交易数据
        transactions = []
        for _ in range(config['n_transactions']):
            transaction_size = np.random.randint(5, 11)  # 每条交易选择5到10个商品
            transaction = set(np.random.choice(top_items, transaction_size, replace=False))  # 从高频商品中选

            # 模拟商品间的相关性：例如“牛奶”和“面包”经常一起出现
            if np.random.rand() < config['correlation_strength']:
                # 为了模拟相关商品，我们手动添加一个已知的相关商品对
                if '面包' in transaction and '牛奶' not in transaction:
                    transaction.add('牛奶')
                elif '牛奶' in transaction and '面包' not in transaction:
                    transaction.add('面包')

            transactions.append(list(transaction))

        return transactions

# 示例使用：加载数据并生成合成数据集
groceries_manager = groceriesDataManager()

# 下载并加载Groceries数据集
groceries_transactions = groceries_manager.download_groceries()

# 预处理：获取前100条交易，并只保留频率最高的20个商品
filtered_transactions, top_20_items = groceries_manager.preprocess_groceries(groceries_transactions)

# 打印预处理结果
print(f"预处理后的Groceries数据集（前100条交易，只保留20个最频繁的商品）:\n{filtered_transactions[:5]}")

# 生成更接近真实数据的合成数据集
generator = SyntheticDatasetGenerator(groceries_transactions)
config = {
    'n_transactions': 100,    # 交易数量
    'n_items': 20,            # 商品种类20个
    'avg_transaction_size': 8,# 平均交易大小8
    'correlation_strength': 0.6  # 商品相关性（例如面包和牛奶的相关性）
}
synthetic_transactions = generator.generate_dataset(config)

# 打印合成数据集示例
print(f"\n生成的更接近真实数据的合成数据集（前5条交易）:\n{synthetic_transactions[:5]}")

# 第三部分：实验与分析

# 1. 生成合成数据集并处理
generator = SyntheticDatasetGenerator(groceries_transactions)
config = {
    'n_transactions': 100,
    'n_items': 20,
    'avg_transaction_size': 8,
    'noise_level': 0.1,
    'correlation_strength': 0.6
}
synthetic_transactions = generator.generate_dataset(config)

# 2. 处理Groceries数据集
data_manager = groceriesDataManager()
groceries_transactions = data_manager.download_groceries()

# 保留前100条交易，并只保留出现频率最高的20个商品
item_counts = Counter(item for transaction in groceries_transactions for item in transaction)
top_20_items = [item for item, _ in item_counts.most_common(20)]
filtered_transactions = [
    [item for item in transaction if item in top_20_items]
    for transaction in groceries_transactions[:100]
]

# 设置支持度阈值并运行暴力破解法
min_supports = [0.1, 0.2, 0.3]
for min_support in min_supports:
    print(f"\n运行暴力破解法，最小支持度={min_support}：")

    # 在合成数据集上
    brute_force = BruteForceFIM(synthetic_transactions, top_20_items)
    start_time = time.time()
    frequent_itemsets_synthetic = brute_force.find_frequent_itemsets(min_support)
    end_time = time.time()
    print(f"合成数据集 - 频繁项集数量: {len(frequent_itemsets_synthetic)}")
    print(f"运行时间: {end_time - start_time} 秒")

    # 在Groceries数据集上
    brute_force = BruteForceFIM(filtered_transactions, top_20_items)
    start_time = time.time()
    frequent_itemsets_groceries = brute_force.find_frequent_itemsets(min_support)
    end_time = time.time()
    print(f"Groceries数据集 - 频繁项集数量: {len(frequent_itemsets_groceries)}")
    print(f"运行时间: {end_time - start_time} 秒")
