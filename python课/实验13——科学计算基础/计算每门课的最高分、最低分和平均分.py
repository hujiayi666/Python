import pandas as pd
# 读取CSV文件，指定第一行为列名
df = pd.read_csv("D:\cxdownload\实验13资料\student_score.csv", header=0)
# 计算每门课的最高分、最低分和平均分
max_scores = {
    '第一门课': df['12'].max(),
    '第二门课': df['45'].max(),
    '第三门课': df['80'].max()
}
min_scores = {
    '第一门课': df['12'].min(),
    '第二门课': df['45'].min(),
    '第三门课': df['80'].min()
}
mean_scores = {
    '第一门课': df['12'].mean(),
    '第二门课': df['45'].mean(),
    '第三门课': df['80'].mean()
}

# 输出每门课的统计信息
for course in ['第一门课', '第二门课', '第三门课']:
    print(f"{course} 最高分: {max_scores[course]}")
    print(f"{course} 最低分: {min_scores[course]}")
    print(f"{course} 平均分: {mean_scores[course]}")
    print("-" * 30)

# 判断第一门课的最低分是否小于12（假设这里是根据你的逻辑进行判断）
if int(min_scores['第一门课']) < 12:
    print("")
else:
    print("修正：第一门课的最低分为12")