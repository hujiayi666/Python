import pandas as pd
import matplotlib.pyplot as plt
# 读取CSV文件数据
df = pd.read_csv("D:\cxdownload\实验13资料\student_score.csv")
course_columns = df.columns[1:4]
# 定义分数段边界
bins = [0, 60, 70, 80, 90, 100]
labels = ['0-60', '60-70', '70-80', '80-90', '90-100']
# 针对每门课程统计各分数段人数
for col in course_columns:
    course_grades = df[col]
    # 使用cut函数划分分数段并统计人数
    grade_counts = pd.cut(course_grades, bins=bins, labels=labels, right=False).value_counts().sort_index()
    if col==12:
        a="第一门"
    elif col==45:
        a="第二门"
    else:
        a="第三门"
    # 绘制折线图
        plt.plot(grade_counts.index, grade_counts.values, marker='o')
        plt.xlabel('分数段')
        plt.ylabel('人数')
        plt.title("课程成绩分数段人数分布")
        plt.xticks(rotation=45)
        plt.show()

     # 绘制条形图
        plt.bar(grade_counts.index, grade_counts.values)
        plt.xlabel('分数段')
        plt.ylabel('人数')
        plt.title("课程成绩分数段人数分布（条形图）")
        plt.xticks(rotation=45)
        plt.show()