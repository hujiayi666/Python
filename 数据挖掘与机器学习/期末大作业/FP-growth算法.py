import pandas as pd
import os
from mlxtend.frequent_patterns import fpgrowth, association_rules
from tqdm import tqdm
# ===============================
# 1️路径设置
# ===============================
base_dir = r"D:\cxdownload\transactions_output"  # 交易表所在文件夹
output_file = r"D:\cxdownload\fp_growth_rules_sample.csv"  # 输出关联规则 CSV
min_support = 0.001  # 可自行调节
min_confidence = 0.2  # 可自行调节
max_rows = 5000  # 每张表只取前 50000 条记录

# ===============================
# 2️⃣ 获取所有交易表文件
# ===============================
transaction_files = [f for f in os.listdir(base_dir) if f.endswith(".csv")]
all_rules = []

# ===============================
# 3️⃣ 遍历每张交易表进行 FP-Growth 挖掘
# ===============================
for file_name in tqdm(transaction_files, desc="Processing transaction tables"):
    file_path = os.path.join(base_dir, file_name)
    df = pd.read_csv(file_path)
    # 限制处理的行数
    df = df.head(max_rows)
    # 判断是全量、按月、还是按小时表
    if 'month' in df.columns:
        time_label = 'month'
    elif 'hour_bin' in df.columns:
        time_label = 'hour_bin'
    else:
        time_label = None
    # 按 user_id 分组，将每个用户的商品列表组合成一个列表
    grouped = df.groupby('user_id')['item_id'].apply(list).tolist()
    if len(grouped) == 0:
        print(f"⚠️ {file_name} 没有交易数据，跳过")
        continue
    # FP-Growth 需要 one-hot 编码
    all_items = sorted({item for sublist in grouped for item in sublist})
    encoded_vals = []
    for transaction in grouped:
        encoded_vals.append([1 if item in transaction else 0 for item in all_items])
    oht_df = pd.DataFrame(encoded_vals, columns=all_items)

    # ===============================
    # 4️⃣ FP-Growth 挖掘频繁项集
    # ===============================
    frequent_itemsets = fpgrowth(oht_df, min_support=min_support, use_colnames=True)
    if frequent_itemsets.empty:
        print(f"⚠️ {file_name} 没有生成频繁项集")
        continue

    # ===============================
    # 5️⃣ 生成关联规则
    # ===============================
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    if rules.empty:
        print(f"⚠️ {file_name} 没有生成关联规则")
        continue

    # 添加来源表、时间信息列
    rules['source_file'] = file_name
    if time_label:
        rules[time_label] = df[time_label].iloc[0] if time_label in df.columns else None

    all_rules.append(rules)

# ===============================
# 6️⃣ 合并所有规则并保存
# ===============================
if all_rules:
    final_rules = pd.concat(all_rules, ignore_index=True)
    final_rules.to_csv(output_file, index=False)
    print(f"✅ FP-Growth 关联规则（样本前 50000 条）已保存到 {output_file}")
else:
    print("⚠️ 所有表都未生成有效关联规则，请尝试降低 min_support 或 min_confidence")
