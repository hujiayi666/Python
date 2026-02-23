import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 先读取CSV文件
csv_data = pd.read_csv()

csv_data.info()


#总得票数
sum_votes = csv_data [['HarrisSum', 'trumpSum', 'otherSum']].sum()

#候选人得票占比饼图
plt.rcParams['figure.dpi'] = 300
plt.figure(figsize=(10,10))
plt.pie(sum_votes, labels=sum_votes.index, autopct='%1.2f%%')
plt.title('候选人得票占比')
plt.show()

#不同候选人在美国各州的支持人数柱状图
plt.rcParams['figure.dpi'] = 300
harris_support = csv_data.groupby('name')['HarrisNum'].sum()
trump_support = csv_data.groupby('name')['trumpNum'].sum()
other_support = csv_data.groupby('name')['otherNum'].sum()
plt.figure(figsize=(12, 8))

bar_width = 0.25
index = range(len(csv_data ['name'].unique()))
plt.bar(index, harris_support, bar_width, label='Harris')
plt.bar([i + bar_width for i in index], trump_support, bar_width, label='特朗普')
plt.bar([i + bar_width * 2 for i in index], other_support, bar_width, label='其他候选人')

plt.xlabel('州')
plt.xticks(index, csv_data ['name'].unique(), rotation=90)
plt.ylabel('支持人数')

plt.title('不同候选人在美国各州的支持人数')
plt.legend()
plt.show()

# 哈里斯的每个州得票数柱状图

# 这里我先排除总数行即第一行，且假设总数行的'id'字段值为'USA'
df = csv_data [csv_data ['id'] != 'USA']

plt.figure(figsize=(12, 8))
sns.barplot(x='name', y='HarrisSum', data=df)
plt.title('哈里斯的每个州得票数柱状图')
plt.xlabel('州')
plt.ylabel('得票数')
plt.xticks(rotation=90)  # 旋转x轴标签防止互相重叠
plt.tight_layout()
plt.show()


#哈里斯的每个州赢得的选举人票数占比饼图
harris_num = df[df['HarrisNum'] > 0][['name', 'HarrisNum']]
plt.figure(figsize=(8, 8))
plt.pie(harris_num['HarrisNum'],labels=harris_num['name'],autopct='%1.1f%%', startangle=140)
plt.title('哈里斯的每个州赢得的选举人票数占比饼图')
plt.show()

#同理得到以下两图
# 特朗普的每个州得票数柱状图
plt.figure(figsize=(12, 8))
sns.barplot(x='name', y='trumpSum', data=df)
plt.title('特朗普的每个州得票数柱状图')
plt.xlabel('州')
plt.ylabel('得票数')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 特朗普的赢得的选举人票数占比饼图
trump_num = df[df['trumpNum'] > 0][['name', 'trumpNum']]
plt.figure(figsize=(8, 8))
plt.pie(trump_num['trumpNum'],labels=trump_num['name'],autopct='%1.1f%%', startangle=140)
plt.title('特朗普的赢得的选举人票数占比饼图')
plt.show()


# 七个摇摆州的哈里斯、特朗普、其他候选人得票率对比饼图
swing_states = ['亚利桑那', '内华达', '佐治亚', '密歇根', '北卡罗来纳', '宾夕法尼亚', '威斯康星']
df_swing = df[df['name'].isin(swing_states)]

for state in swing_states:
    state_data = df_swing[df_swing['name'] == state]
    plt.figure(figsize=(8, 8))
    labels = ['Harris', 'Trump', 'Other']
    sizes=[state_data.iloc[0]['HarrisRate'],state_data.iloc[0]['trumpRate'], state_data.iloc[0]['otherRate']]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'{state}的Harris、Trump、Other得票率对比饼图')
    plt.show()



