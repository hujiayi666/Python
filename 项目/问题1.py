import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置中文字体
font_path = 'C:/Windows/Fonts/simsun.ttc'  # 具体路径请根据您的系统调整
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 读取节点数据
node_file_path =r"C:\Users\hujia\Desktop\2024江西财经大学数学建模竞赛赛题\2024.csv"
node_data = pd.read_csv(node_file_path, encoding='gbk')

# 读取路线数据
route_file_path =r"C:\Users\hujia\Desktop\2024江西财经大学数学建模竞赛赛题\城市地点和道路信息.csv"
route_data = pd.read_csv(route_file_path, encoding='gbk')

# 清理和选择节点数据，移除包含NaN值的行
cleaned_node_data = node_data.dropna(subset=['全市路口节点标号', '路口的横坐标X', '路口的纵坐标Y'])

# 移除包含NaN值的边数据
cleaned_route_data = route_data.dropna(subset=['路线起点(节点）标号', '路线终点（节点）标号'])

# 创建一个空的有向图
G = nx.DiGraph()

# 添加节点
for index, row in cleaned_node_data.iterrows():
    G.add_node(row['全市路口节点标号'], pos=(row['路口的横坐标X'], row['路口的纵坐标Y']))

# 添加边
for index, row in cleaned_route_data.iterrows():
    G.add_edge(row['路线起点(节点）标号'], row['路线终点（节点）标号'], weight=1)  # 假设每条边的权重为1

# 绘制图形
pos = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold', arrowsize=20)
plt.title('城市交通网络图')
plt.show()
