import time
import numpy as np
import requests
from collections import Counter
import itertools


# 频繁项集挖掘的暴力破解法类
class BruteForceFIM:
    def __init__(self, transactions, items):
        self.transactions = transactions
        self.items = sorted(items)  # 排序以便确定性
        self.n = len(items)  # 商品总数
        self.m = len(transactions)  # 交易总数

    def generate_all_itemsets(self):
        """生成所有可能的非空项集 (从1项集到最大项集)"""
        all_itemsets = []
        # 生成从1到n项集的所有组合
        for r in range(1, self.n + 1):  # 从1项集到n项集
            for itemset in itertools.combinations(self.items, r):
                all_itemsets.append(set(itemset))  # 将每个项集转为集合
        return all_itemsets

    def calculate_support(self, itemset):
        """计算项集支持度"""
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


# 数据集处理类
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
            return []

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


# 生成合成数据集的类
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


# 第三部分：实验与分析

# 1. 生成合成数据集并处理
groceries_manager = groceriesDataManager()
groceries_transactions = groceries_manager.download_groceries()

generator = SyntheticDatasetGenerator(groceries_transactions)
config = {
    'n_transactions': 100,
    'n_items': 20,
    'avg_transaction_size': 8,
    'correlation_strength': 0.6
}

synthetic_transactions = generator.generate_dataset(config)

# 2. 处理Groceries数据集
filtered_transactions, top_20_items = groceries_manager.preprocess_groceries(groceries_transactions)

# 输出预处理后的Groceries数据集（前100条交易，只保留20个最频繁的商品）
print(f"\n预处理后的Groceries数据集（前100条交易，只保留20个最频繁的商品）:\n{filtered_transactions[:5]}")

# 查找并输出频繁项集
min_support =0.1
brute_force = BruteForceFIM(filtered_transactions, top_20_items)
frequent_itemsets_groceries = brute_force.find_frequent_itemsets(min_support)

print(f"\n找到的频繁项集 (最小支持度={min_support}):")
for itemset, support in frequent_itemsets_groceries:
    print(f"项集: {itemset}, 支持度: {support}")

# 设置支持度阈值并运行暴力破解法
min_supports = [0.1, 0.2, 0.3]  # 设置不同的最小支持度
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

