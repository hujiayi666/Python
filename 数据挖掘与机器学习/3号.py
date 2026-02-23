import requests
import itertools
import numpy as np
from collections import Counter


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

        # 输出符合条件的频繁项集
        return frequent_itemsets


# 示例使用：加载数据并生成频繁项集
groceries_manager = groceriesDataManager()

# 下载并加载Groceries数据集
groceries_transactions = groceries_manager.download_groceries()

# 预处理：获取前100条交易，并只保留频率最高的20个商品
filtered_transactions, top_20_items = groceries_manager.preprocess_groceries(groceries_transactions)

# 打印预处理结果
print(f"\n预处理后的Groceries数据集（前100条交易，只保留20个最频繁的商品）:\n{filtered_transactions[:5]}")

# 设置最小支持度为0.1
min_support = 0.1

# 创建 BruteForceFIM 实例
brute_force = BruteForceFIM(filtered_transactions, top_20_items)

# 查找频繁项集
frequent_itemsets = brute_force.find_frequent_itemsets(min_support)

# 输出找到的频繁项集
print(f"\n找到的频繁项集 (最小支持度={min_support}):")
for itemset, support in frequent_itemsets:
    print(f"项集: {itemset}, 支持度: {support}")
