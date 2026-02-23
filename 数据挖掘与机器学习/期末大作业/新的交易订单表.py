import pandas as pd
import os

# ===============================
# 1️路径设置
# ===============================
data_path = r"D:\cxdownload\user_behavior_time_resampled\user_behavior_time_resampled.csv"
output_dir = r"D:\cxdownload\transactions_output"
# 如果输出文件夹不存在，就创建
os.makedirs(output_dir, exist_ok=True)

# ===============================
# 2️读取原始数据
# ===============================
df = pd.read_csv(data_path)

# 只保留下单行为
order_df = df[df['action_type'] == 'order'].copy()
order_df = order_df[['user_id', 'item_id', 'time_stamp', 'timestamp']]

# ===============================
# 3️全量订单交易表
# ===============================
transactions_all = order_df[['user_id', 'item_id']].drop_duplicates()

transactions_all.to_csv(
    os.path.join(output_dir, "transactions_all.csv"),
    index=False
)
print("✅ 全量订单交易表已保存")

# ===============================
# 4️⃣ 按月份订单交易表（一个表，所有月份）
# time_stamp = 月*100 + 日
# ===============================
order_df['month'] = order_df['time_stamp'] // 100
transactions_month = order_df[['user_id', 'item_id', 'month']].drop_duplicates()
transactions_month.to_csv(
    os.path.join(output_dir, "transactions_by_month.csv"),
    index=False
)
print("✅ 按月份订单交易表已保存")
print("📌 实际存在的月份：")
print(transactions_month['month'].value_counts().sort_index())

# ===============================
# 5️⃣ 按每天 2 小时订单交易表
# timestamp = 当天已过去的秒数
# ===============================
order_df['hour'] = (order_df['timestamp'] // 3600).astype(int)
order_df['hour_bin'] = (order_df['hour'] // 2) * 2
transactions_time = order_df[['user_id', 'item_id', 'hour_bin']].drop_duplicates()
transactions_time.to_csv(
    os.path.join(output_dir, "transactions_by_2hour.csv"),
    index=False)
print("✅ 按每天 2 小时订单交易表已保存")
print("📌 实际存在的 2 小时时段：")
print(sorted(transactions_time['hour_bin'].unique()))
