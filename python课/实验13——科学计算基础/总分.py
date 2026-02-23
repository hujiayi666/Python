import pandas as pd

# 读取CSV文件，假设文件中第一行为列名，自动解析
df = pd.read_csv("D:\cxdownload\实验13资料\student_score.csv")

# 找出数据类型为整数的列，这里假设标识列是整数类型，认为第一个找到的整数类型列就是标识列（根据实际情况调整）
id_column = None
for col in df.columns:
    if df[col].dtype == 'int64':  # 假设是int64类型，也可能是其他整数类型如int32等，按实际调整
        id_column = col
        break

# 找出成绩相关的列（这里简单假设除了标识列，其余都是成绩列，可根据实际调整）
score_columns = [col for col in df.columns if col!= id_column]

# 计算每个学生三门课程的总分
df['total_score'] = df[score_columns].sum(axis=1)

# 打印输出每个学生的学号（这里就是找到的标识列）和总分情况
print(df[[id_column, 'total_score']])