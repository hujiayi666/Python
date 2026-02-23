import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 第一步：加载并预处理数据
data_path =r"C:\Users\hujia\Downloads\ddfdc775-f999-4439-8c05-caa7c2c3cb55_Data.csv"
data = pd.read_csv(data_path)

# 显示数据的前几行
print("数据加载成功: \n", data.head())

# 第二步：动态地图可视化
def dynamic_map(data):
    # 筛选年份列（假设年份是1999到2023）和国家名称列
    year_columns = [str(year) for year in range(1999, 2024)]
    data_years = data[["Country Name"] + year_columns]

    # 将年份列展开
    data_melted = data_years.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
    data_melted = data_melted.dropna()  # 去掉空值
    data_melted["Year"] = data_melted["Year"].astype(int)  # 将年份转换为整数类型
    data_melted["GDP"] = pd.to_numeric(data_melted["GDP"], errors="coerce")  # 将GDP转换为数值类型
    data_melted = data_melted.dropna()

    # 绘制动态地图
    fig = px.choropleth(
        data_frame=data_melted,
        locations="Country Name",  # 使用国家名称列
        locationmode="country names",  # 按国家名称定位
        color="GDP",  # 用于着色的GDP列
        animation_frame="Year",  # 按年份动画显示
        title="全球GDP变化动态地图",
        color_continuous_scale=px.colors.sequential.Plasma
    )
    fig.show()

# 第三步：3D柱状图可视化
def bar_chart_3d(data, top_n=None):
    # 筛选年份列
    year_columns = [str(year) for year in range(1999, 2024)]
    data_years = data[["Country Name"] + year_columns]
    data_melted = data_years.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
    data_melted = data_melted.dropna()
    data_melted["Year"] = data_melted["Year"].astype(int)
    data_melted["GDP"] = pd.to_numeric(data_melted["GDP"], errors="coerce")
    data_melted = data_melted.dropna()

    if top_n:
        # 获取GDP最高的前N个国家
        top_countries = data_melted.groupby("Country Name")["GDP"].mean().nlargest(top_n).index
        data_melted = data_melted[data_melted["Country Name"].isin(top_countries)]

    fig = px.bar(
        data_melted,
        x="Country Name",
        y="GDP",
        color="Year",
        title=f"{'前' + str(top_n) if top_n else '所有'}国家3D柱状图"
    )
    fig.show()

# 第四步：前10国家的折线图
def line_plot_top(data, top_n=10):
    # 筛选年份列
    year_columns = [str(year) for year in range(1999, 2024)]
    data_years = data[["Country Name"] + year_columns]
    data_melted = data_years.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")
    data_melted = data_melted.dropna()
    data_melted["Year"] = data_melted["Year"].astype(int)
    data_melted["GDP"] = pd.to_numeric(data_melted["GDP"], errors="coerce")
    data_melted = data_melted.dropna()

    # 获取GDP最高的前N个国家
    top_countries = data_melted.groupby("Country Name")["GDP"].mean().nlargest(top_n).index
    filtered_data = data_melted[data_melted["Country Name"].isin(top_countries)]

    fig = px.line(
        filtered_data,
        x="Year",  # x轴：年份
        y="GDP",   # y轴：GDP值
        color="Country Name",  # 按国家区分颜色
        title=f"前{top_n}国家GDP变化折线图"
    )
    fig.show()

# 第五步：环状比例图可视化
def ring_chart(data, top_n=None):
    # 筛选年份列
    year_columns = [str(year) for year in range(1999, 2024)]
    data_years = data[["Country Name"] + year_columns]
    data_latest = data_years[["Country Name", "2023"]]
    data_latest["GDP"] = pd.to_numeric(data_latest["2023"], errors="coerce")
    data_latest = data_latest.dropna()

    if top_n:
        # 获取GDP最高的前N个国家
        data_latest = data_latest.nlargest(top_n, "GDP")

    labels = data_latest["Country Name"]
    values = data_latest["GDP"]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, startangle=90, counterclock=False, wedgeprops={'width': 0.3}, autopct='%1.1f%%')
    ax.set_title(f"{'前' + str(top_n) if top_n else '所有'}国家GDP分布环状图")
    plt.show()

# 第六步：中美GDP预测
def forecast_gdp(data, country, years_ahead=20):
    # 筛选特定国家的数据
    year_columns = [str(year) for year in range(1999, 2024)]
    country_data = data[data['Country Name'] == country][["Country Name"] + year_columns].melt(
        id_vars=["Country Name"], var_name="Year", value_name="GDP"
    )
    country_data = country_data.dropna()
    country_data["Year"] = country_data["Year"].astype(int)
    country_data["GDP"] = pd.to_numeric(country_data["GDP"], errors="coerce")

    X = np.array(country_data['Year']).reshape(-1, 1)
    y = np.array(country_data['GDP']).reshape(-1, 1)

    # 使用线性回归模型进行预测
    model = LinearRegression()
    model.fit(X, y)

    # 生成未来年份
    future_years = np.array(range(country_data['Year'].max() + 1, country_data['Year'].max() + years_ahead + 1)).reshape(-1, 1)
    predictions = model.predict(future_years)

    # 绘制结果
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['GDP'], label='历史GDP')
    plt.plot(future_years, predictions, label=f'预测({years_ahead}年)', linestyle='--')
    plt.title(f"{country} GDP预测")
    plt.xlabel('年份')
    plt.ylabel('GDP')
    plt.legend()
    plt.show()

# 示例使用
dynamic_map(data)
bar_chart_3d(data)
bar_chart_3d(data, top_n=20)
line_plot_top(data)
ring_chart(data)
ring_chart(data, top_n=20)
forecast_gdp(data, "United States")
forecast_gdp(data, "China")