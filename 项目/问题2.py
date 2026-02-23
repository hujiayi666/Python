import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import chardet

# 读取CSV文件
file_path =r"C:\Users\hujia\Desktop\2024江西财经大学数学建模竞赛赛题\城市地点和道路信息.csv"

data = pd.read_csv(file_path, encoding='GB2312')

# 打印前几行数据样本以检查列名
print(data.head())

# 清洗列名中的空格和特殊字符
data.columns = data.columns.str.strip()
data.columns = data.columns.str.replace('（', '(').str.replace('）', ')')

# 打印清洗后的列名
print("Cleaned Columns in the data frame:")
print(data.columns)

# 手动确认并设置“距离”列
# 假设“Unnamed: 2”列是距离列
data.rename(columns={'Unnamed: 2': '距离'}, inplace=True)

# 确认列名正确
expected_columns = ['路线起点(节点)标号', '路线终点(节点)标号', '距离']
for col in expected_columns:
    if col not in data.columns:
        print(f"Missing expected column: {col}")
        exit()

# 去除无关列并填充NaN值（这里用0填充距离列中的NaN值）
data = data[expected_columns].fillna(0)

# 初始化图
G = nx.Graph()

# 添加节点和边
for index, row in data.iterrows():
    G.add_edge(int(row['路线起点(节点)标号']), int(row['路线终点(节点)标号']), weight=row['距离'])

# 绘制城市交通网络图
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)

# 绘制节点和边
nx.draw_networkx_edges(G, pos, alpha=0.5)

# 消防站节点
fire_stations = [1, 2, 3, 4]

# 计算每个节点到各消防站的最短路径距离
reachable_nodes = {station: {} for station in fire_stations}

for station in fire_stations:
    lengths = nx.single_source_dijkstra_path_length(G, station)
    reachable_nodes[station] = lengths
    print(f"Reachable nodes from station {station}: {lengths}")

# 计算8分钟内可到达的最大距离
max_distance = 8 * (60 / 60)
print(f"Maximum reachable distance in 8 minutes: {max_distance} km")

# 分配节点给最近的消防站
node_assignment = {}

for node in G.nodes:
    min_distance = float('inf')
    assigned_station = None
    for station in fire_stations:
        if node in reachable_nodes[station] and reachable_nodes[station][node] <= max_distance:
            distance = reachable_nodes[station][node]
            if distance < min_distance:
                min_distance = distance
                assigned_station = station
    if assigned_station is not None:
        node_assignment[node] = assigned_station
        print(f"Node {node} assigned to station {assigned_station} with distance {min_distance}")

# 检查并移除未分配消防站的节点
node_assignment = {node: station for node, station in node_assignment.items() if station is not None}

# 可视化管辖范围
color_map = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'purple'
}

# 绘制节点
for station in fire_stations:
    nodes = [node for node, assigned_station in node_assignment.items() if assigned_station == station]
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=color_map[station], node_size=300, label=f'消防站 {station}')

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# 添加图例
plt.legend(scatterpoints=1, loc='upper left', fontsize=12)
plt.title('城市消防站管辖范围图')
plt.show()

# 打印任务分配结果
print("节点分配结果：")
for node, station in node_assignment.items():
    print(f"节点 {node} 分配给消防站 {station}")
