import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
# 文件路径
transactions_file = r"D:\cxdownload\transactions_output1\transactions_month_5.csv"
# 读取交易表
transactions_df = pd.read_csv(transactions_file)
# 只取前 64000 条交易测试
transactions_sample = transactions_df.head(40000)
# 按 user_id 聚合，生成每个用户的商品列表
user_transactions = transactions_sample.groupby('user_id')['item_id'].apply(list).tolist()
print(f"处理后的交易条数: {len(user_transactions)}")
# TransactionEncoder 转换成 One-Hot 编码
te = TransactionEncoder()
te_ary = te.fit(user_transactions).transform(user_transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
# 设置支持度和置信度
min_support = 0.0005  # 0.05%
min_confidence = 0.0003
# 生成频繁项集
frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)
if frequent_itemsets.empty:
    print("没有生成频繁项集，尝试降低 min_support")
else:
    print(f"频繁项集生成成功，数量: {len(frequent_itemsets)}")
    # 生成关联规则
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    if rules.empty:
        print("没有生成关联规则")
    else:
        print(f"关联规则生成成功，数量: {len(rules)}")
        print(rules.head(10))
