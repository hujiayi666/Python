#动态GDP柱状图绘制
#导包
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
from pyecharts.charts import Timeline
from pyecharts.globals import ThemeType
#读取数据
f=open("D:/1960-2019全球GDP数据.csv","r",encoding="GB2312")
#读取每一行内容
data_lines=f.readlines()
f.close()#关闭文件
#删除第一行
data_lines.pop(0)
#将数据转换为字典
data_dict={}
for line in data_lines:
    year=int(line.split(",")[0])    #年份
    country=line.split(",")[1]      #国家
    GDP=float(line.split(",")[2])   #GDP数据
    try:
        data_dict[year].append([country, GDP])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, GDP])
#创建时间线
timeline=Timeline({"theme":ThemeType.LIGHT})
#排序年份
sorted_year_list=sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    #取出前八
    year_data=data_dict[year][0:10]
    x_data=[]
    y_data=[]
    for country_GDP in year_data:
        x_data.append(country_GDP[0])
        y_data.append(country_GDP[1]/100000000)
    #构建柱状图
    bar=Bar()
    x_data.reverse()#再次反转
    y_data.reverse()#再次反转
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿美元)",y_data,label_opts=LabelOpts(position="right"))
    #反转xy轴
    bar.reversal_axis()
    #设置全局配置项
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP前八名"),
        legend_opts=LegendOpts(is_show=True),
        toolbox_opts=ToolboxOpts(is_show=True),
        visualmap_opts=VisualMapOpts(is_show=True) )
    timeline.add(bar,str(year))
#自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
#绘图
timeline.render("动态GDP柱状图.html")






























