import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 读取CSV文件
file_path =r"C:\Users\hujia\Desktop\2024江西财经大学数学建模竞赛赛题\城市地点和道路信息.csv"
data = pd.read_csv(file_path, encoding='GB2312')

# 清洗列名中的空格和特殊字符
data.columns = data.columns.str.strip()
data.columns = data.columns.str.replace('（', '(').str.replace('）', ')')

# 打印清洗后的列名和数据样本
print("Cleaned Columns in the data frame:")
print(data.columns)
print("Data sample:")
print(data.head())

# 手动确认并设置“距离”列
data.rename(columns={'Unnamed: 2': '距离'}, inplace=True)

# 确认列名正确
expected_columns = ['路线起点(节点)标号', '路线终点(节点)标号', '距离']
for col in expected_columns:
    if col not in data.columns:
        print(f"Missing expected column: {col}")
        exit()

# 检查距离列中的NaN值
print("Checking NaN values in '距离' column:")
print(data['距离'].isna().sum())

# 将距离列中的NaN值替换为0
data['距离'].fillna(0, inplace=True)

# 去除包含NaN值的行
data.dropna(subset=['路线起点(节点)标号', '路线终点(节点)标号'], inplace=True)

# 打印处理后的数据样本
print("Processed data sample:")
print(data.head())

# 初始化图
G = nx.Graph()

# 添加节点和边，并打印信息以确认
print("Adding edges to graph:")
for index, row in data.iterrows():
    try:
        u = int(row['路线起点(节点)标号'])
        v = int(row['路线终点(节点)标号'])
        weight = row['距离']
        G.add_edge(u, v, weight=weight)
        print(f"Added edge: {u} --({weight})--> {v}")
    except ValueError as e:
        print(f"Skipping row due to error: {e}")

# 打印图的节点和边
print("Graph nodes:")
print(G.nodes())
print("Graph edges:")
print(G.edges(data=True))

# 获取节点位置
pos = nx.spring_layout(G)

# 打印节点和位置以确保正确
print("Nodes and positions:")
for node, p in pos.items():
    print(f"Node {node}: Position {p}")

# 提取节点位置数据作为K-means的输入
nodes = list(G.nodes)
node_positions = np.array([pos[node] for node in nodes])

# 打印节点位置数组以确认
print("Node positions array:")
print(node_positions)

# 确保node_positions不为空
if node_positions.shape[0] == 0:
    print("Error: node_positions array is empty.")
    exit()

# K-means聚类
def kmeans(X, k, max_iters=100):
    # 随机初始化中心点
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    for _ in range(max_iters):
        # 计算每个点到各个中心点的距离
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        # 找到每个点最近的中心点
        closest_centroids = np.argmin(distances, axis=1)
        # 更新中心点
        new_centroids = np.array([X[closest_centroids == i].mean(axis=0) for i in range(k)])
        # 如果中心点没有变化，停止迭代
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, closest_centroids

# 应用K-means算法
k = 4
centroids, closest_centroids = kmeans(node_positions, k)

# 可视化新布局
plt.figure(figsize=(12, 8))

# 绘制节点和边
nx.draw_networkx_edges(G, pos, alpha=0.5)

# 绘制原始节点
nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color='lightblue', node_size=300)

# 绘制新消防站位置
for i, centroid in enumerate(centroids):
    plt.scatter(centroid[0], centroid[1], s=1000, c=f'C{i}', label=f'新消防站 {i+1}')

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# 添加图例
plt.legend(scatterpoints=1, loc='upper left', fontsize=12)
plt.title('城市消防站重新布局图')
plt.show()

# 打印新消防站位置
print("新消防站位置：")
for i, centroid in enumerate(centroids):
    print(f"新消防站 {i+1}: {centroid}")

# 计算每个节点到最近新消防站的距离
max_distance = 8 * (60 / 60)  # 8分钟可到达的最大距离
node_assignment = {}

for node in G.nodes:
    min_distance = float('inf')
    assigned_station = None
    for i, centroid in enumerate(centroids):
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
        print(f"节点 {node} 分配给新消防站 {station}，距离：{np.linalg.norm(np.array(pos[node]) - centroids[station-1])}")
    else:
        print(f"节点 {node} 无法在8分钟内到达任何消防站")

# 检查是否有节点未被分配
unassigned_nodes = [node for node, station in node_assignment.items() if station is None]
if unassigned_nodes:
    print("以下节点未能在8分钟内到达任何消防站：", unassigned_nodes)
else:
    print("所有节点都能在8分钟内到达至少一个消防站。")
