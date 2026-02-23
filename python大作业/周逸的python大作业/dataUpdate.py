import pandas as pd

# 读取 CSV 文件
file_path = r"D:\cxdownload\实验14资料\ddfdc775-f999-4439-8c05-caa7c2c3cb55_Data.csv"  # 替换为你的文件路径
data = pd.read_csv(file_path)

# 替换 ".." 为 NaN
data_cleaned = data.replace('..', pd.NA)

# 保存清理后的文件
cleaned_file_path = r"D:\cxdownload\实验14资料" # 替换为保存文件的位置
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"清理完成，文件已保存到：{cleaned_file_path}")
