import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from tqdm import tqdm
import os
# 文件路径
base_dir = r"D:\cxdownload\transactions_output"  # 三张交易表所在文件夹
user_info_file = r"D:\cxdownload\user_behavior_time_resampled\user_info.csv"
output_file = r"D:\cxdownload\marketing_recommendations.csv"
# 参数
min_support = 0.0005
min_confidence = 0.05

# 读取用户信息
user_info = pd.read_csv(user_info_file)


# 函数：生成 Apriori 关联规则
def generate_rules(transactions_df, time_col=None):
    # 如果有时间列，则先聚合
    if time_col:grouped = transactions_df.groupby(time_col)
    else:grouped = [(None, transactions_df)]
    all_rules = []
    for time_label, df_group in tqdm(grouped, desc="Processing transactions"):
        # 将每个用户的购买商品列表聚合
        transactions = df_group.groupby('user_id')['item_id'].apply(list).tolist()
        # 安全处理：空交易表跳过
        if len(transactions) == 0:
            continue
        # one-hot 编码
        from mlxtend.preprocessing import TransactionEncoder
        te = TransactionEncoder()
        te_array = te.fit(transactions).transform(transactions)
        df_onehot = pd.DataFrame(te_array, columns=te.columns_)
        # 频繁项集
        frequent_itemsets = apriori(df_onehot, min_support=min_support, use_colnames=True)
        if frequent_itemsets.empty:
            continue
        # 关联规则
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
        if rules.empty:
            continue
        # 添加时间列
        if time_col:
            rules[time_col] = time_label
        all_rules.append(rules)
    if all_rules:
        return pd.concat(all_rules, ignore_index=True)
    else:
        return pd.DataFrame()  # 返回空表


# 挖掘三张交易表
transaction_files = {
    "all": "transactions_all.csv",
    "monthly": "transactions_by_month.csv",
    "hourly": "transactions_by_2hour.csv"
}
rules_list = []
for key, file_name in transaction_files.items():
    file_path = os.path.join(base_dir, file_name)
    df = pd.read_csv(file_path)
    if key == "monthly":rules = generate_rules(df, time_col='month')
    elif key == "hourly":rules = generate_rules(df, time_col='hour_bin')
    else:rules = generate_rules(df)
    if not rules.empty:rules_list.append(rules)
# 合并所有规则
if rules_list:all_rules_df = pd.concat(rules_list, ignore_index=True)
else:all_rules_df = pd.DataFrame()
# 将规则与用户信息关联（只取 antecedent 商品）
if not all_rules_df.empty:
    recommendations = []
    for _, row in all_rules_df.iterrows():
        antecedent_items = list(row['antecedents'])
        consequent_items = list(row['consequents'])
        # 找到购买了 antecedent 商品的用户
        users = df[df['item_id'].isin(antecedent_items)]['user_id'].unique()
        user_data = user_info[user_info['user_id'].isin(users)]
        for _, u in user_data.iterrows():
            for ante_item in antecedent_items:
                for cons_item in consequent_items:
                    rec = {"user_id": u['user_id'],"age_range": u['age_range'],"gender": u['gender'],"antecedent_item": ante_item,"recommended_item": cons_item}
                    # 添加时间信息
                    if 'month' in row:rec['time_period'] = row['month']
                    elif 'hour_bin' in row:rec['time_period'] = row['hour_bin']
                    else:rec['time_period'] = None
                    recommendations.append(rec)
    recommendations_df = pd.DataFrame(recommendations)
    recommendations_df.to_csv(output_file, index=False)
    print(f"营销推荐 CSV 已生成: {output_file}")
else:
    print("没有生成有效的关联规则。")
