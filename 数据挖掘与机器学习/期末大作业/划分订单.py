import pandas as pd
import os

# ===============================
# 1️⃣ 路径设置
# ===============================
data_path = r"D:\cxdownload\user_behavior_time_resampled\user_behavior_time_resampled.csv"
output_dir = r"D:\cxdownload\transactions_output1"
os.makedirs(output_dir, exist_ok=True)

# ===============================
# 2️⃣ 读取原始数据
# ===============================
df = pd.read_csv(data_path)

# 只保留下单行为
order_df = df[df['action_type'] == 'order'].copy()
order_df = order_df[['user_id', 'item_id', 'time_stamp', 'timestamp']]

# ===============================
# 3️⃣ 全量订单交易表
# ===============================
transactions_all = order_df[['user_id', 'item_id']].drop_duplicates()
transactions_all.to_csv(os.path.join(output_dir, "transactions_all.csv"), index=False)
print("✅ 全量订单交易表已保存")

# ===============================
# 4️⃣ 按月份拆分成独立表
# ===============================
order_df['month'] = order_df['time_stamp'] // 100
months = sorted(order_df['month'].unique())

for m in months:
    month_df = order_df[order_df['month'] == m][['user_id', 'item_id', 'month']].drop_duplicates()
    month_df.to_csv(os.path.join(output_dir, f"transactions_month_{m}.csv"), index=False)
    print(f"✅ {m} 月交易表已保存，条数: {len(month_df)}")

print("📌 月份完成拆分：", months)

# ===============================
# 5️⃣ 按每天 2 小时拆分成独立表
# timestamp = 当天已过去的秒数
# ===============================
order_df['hour'] = (order_df['timestamp'] // 3600).astype(int)
order_df['hour_bin'] = (order_df['hour'] // 2) * 2
hour_bins = sorted(order_df['hour_bin'].unique())

for h in hour_bins:
    hour_df = order_df[order_df['hour_bin'] == h][['user_id', 'item_id', 'hour_bin']].drop_duplicates()
    hour_df.to_csv(os.path.join(output_dir, f"transactions_hour_{h}.csv"), index=False)
    print(f"✅ {h} 时段交易表已保存，条数: {len(hour_df)}")

print("📌 2 小时时段完成拆分：", hour_bins)
