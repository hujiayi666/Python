import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# 读取两个CSV文件
file_path1 =r"C:\Users\hujia\Desktop\2024江西财经大学数学建模竞赛赛题\城市地点和道路信息.csv"
file_path2 = r"C:\Users\hujia\Desktop\2024江西财经大学数学建模竞赛赛题\2024.csv"

data1 = pd.read_csv(file_path1, encoding='GB2312')
data2 = pd.read_csv(file_path2, encoding='GB2312')

# 打印数据样本以检查列名和内容
print("Data1 sample:")
print(data1.head())
print("Data2 sample:")
print(data2.head())

# 清洗列名中的空格和特殊字符
data1.columns = data1.columns.str.strip()
data1.columns = data1.columns.str.replace('（', '(').str.replace('）', ')')

data2.columns = data2.columns.str.strip()
data2.columns = data2.columns.str.replace('（', '(').str.replace('）', ')')

# 打印清洗后的列名
print("Cleaned Columns in Data1:")
print(data1.columns)
print("Cleaned Columns in Data2:")
print(data2.columns)

# 合并数据（假设数据结构相同，可以根据需要调整合并方式）
data = pd.concat([data1, data2], ignore_index=True)

# 手动确认并设置“距离”列
data.rename(columns={'Unnamed: 2': '距离'}, inplace=True)

# 去除包含NaN值的行
data.dropna(subset=['路线起点(节点)标号', '路线终点(节点)标号'], inplace=True)
data['距离'].fillna(0, inplace=True)

# 打印处理后的数据样本
print("Processed data sample:")
print(data.head())

# 初始化图
G = nx.Graph()

# 添加节点和边
for index, row in data.iterrows():
    u = int(row['路线起点(节点)标号'])
    v = int(row['路线终点(节点)标号'])
    weight = row['距离']
    G.add_edge(u, v, weight=weight)

# 获取节点位置
pos = nx.spring_layout(G)

# 提取节点位置数据
nodes = list(G.nodes)
node_positions = np.array([pos[node] for node in nodes])

# 初始消防站位置（随机选择k个节点作为初始消防站）
k = 4
initial_fire_stations = random.sample(nodes, k)
initial_centroids = np.array([pos[node] for node in initial_fire_stations])

# 模拟退火参数
initial_temperature = 1000
final_temperature = 1
cooling_rate = 0.99

# 计算给定消防站位置的质量（所有节点到最近消防站的最大距离）
def compute_quality(centroids):
    max_distance = 0
    for node in nodes:
        min_distance = float('inf')
        for centroid in centroids:
            distance = np.linalg.norm(np.array(pos[node]) - centroid)
            if distance < min_distance:
                min_distance = distance
        if min_distance > max_distance:
            max_distance = min_distance
    return max_distance

# 模拟退火算法
current_temperature = initial_temperature
current_solution = initial_centroids
current_quality = compute_quality(current_solution)
best_solution = current_solution
best_quality = current_quality

while current_temperature > final_temperature:
    new_solution = current_solution.copy()
    # 随机移动一个消防站
    random_index = random.randint(0, k-1)
    new_station_position = pos[random.choice(nodes)]
    new_solution[random_index] = new_station_position
    new_quality = compute_quality(new_solution)

    # 根据接受概率决定是否接受新解
    if new_quality < current_quality:
        current_solution = new_solution
        current_quality = new_quality
        if new_quality < best_quality:
            best_solution = new_solution
            best_quality = new_quality
    else:
        acceptance_probability = np.exp((current_quality - new_quality) / current_temperature)
        if random.uniform(0, 1) < acceptance_probability:
            current_solution = new_solution
            current_quality = new_quality

    # 降低温度
    current_temperature *= cooling_rate

# 可视化优化后的布局
plt.figure(figsize=(12, 8))

# 绘制节点和边
nx.draw_networkx_edges(G, pos, alpha=0.5)

# 绘制原始节点
nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='lightblue', node_size=300)

# 绘制优化后的消防站位置
for i, centroid in enumerate(best_solution):
    plt.scatter(centroid[0], centroid[1], s=1000, c=f'C{i}', label=f'消防站 {i+1}')

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# 添加图例
plt.legend(scatterpoints=1, loc='upper left', fontsize=12)
plt.title('优化后的城市消防站布局图')
plt.show()

# 打印优化后的消防站位置
print("优化后的消防站位置：")
for i, centroid in enumerate(best_solution):
    print(f"消防站 {i+1}: {centroid}")

# 计算每个节点到最近新消防站的距离
max_distance = 8 * (60 / 60)  # 8分钟可到达的最大距离
node_assignment = {}

for node in G.nodes:
    min_distance = float('inf')
    assigned_station = None
    for i, centroid in enumerate(best_solution):
        distance = np.linalg.norm(np.array(pos[node]) - centroid)
        if distance < min_distance:
            min_distance = distance
            assigned_station = i + 1
    if min_distance <= max_distance:
        node_assignment[node] = assigned_station
    else:
        node_assignment[node] = None

# 打印任务分配结果
print("节点分配结果：")
for node, station in node_assignment.items():
    if station is not None:
        print(f"节点 {node} 分配给新消防站 {station}，距离：{np.linalg.norm(np.array(pos[node]) - best_solution[station-1])}")
    else:
        print(f"节点 {node} 无法在8分钟内到达任何消防站")

# 检查是否有节点未被分配
unassigned_nodes = [node for node, station in node_assignment.items() if station is None]
if unassigned_nodes:
    print("以下节点未能在8分钟内到达任何消防站：", unassigned_nodes)
else:
    print("所有节点都能在8分钟内到达至少一个消防站。")
