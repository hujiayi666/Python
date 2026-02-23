"""
演示美日印三国疫情可视化开发
"""
#导包
import json
import pyecharts
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts
#读取文件
f_us=open("D:/美国.txt","r",encoding="UTF-8")
f_jp=open("D:/日本.txt","r",encoding="UTF-8")
f_id=open("D:/印度.txt","r",encoding="UTF-8")
# 读取数据文件
us_data=f_us.read()
jp_data=f_jp.read()
id_data=f_id.read()
#去掉不符合格式的开头
us_data=us_data.replace("jsonp_1629344292311_69436(", "")
jp_data=jp_data.replace("jsonp_1629344292311_69436(", "")
id_data=id_data.replace("jsonp_1629344292311_69436(", "")
#去掉不符合格式的结尾·
us_data=us_data[:-2]
jp_data=jp_data[:-2]
id_data=id_data[:-2]
# 将字符串json转换为python的字典
us_dict=json.loads(us_data)
jp_dict=json.loads(us_data)
id_dict=json.loads(us_data)
#继续读取以减少层级
us_trend=us_dict['data'][0]['trend']
jp_trend=jp_dict['data'][0]['trend']
id_trend=id_dict['data'][0]['trend']
# 从字典中取出x,y轴的数据
#x轴数据
x_date1=us_trend['updateDate'][:314]
x_date2=jp_trend['updateDate'][:314]
x_date3=id_trend['updateDate'][:314]
#y轴数据
y_date1=us_trend['list'][0]['data'][:314]
y_date2=jp_trend['list'][0]['data'][:314]
y_date3=id_trend['list'][0]['data'][:314]
# 调用pyecharts的charts.line功能来生成图表
line=pyecharts.charts.Line()
#填入x轴数据
line.add_xaxis(x_date1)
#填入y轴数据
line.add_yaxis("美国确诊人数",y_date1)
line.add_yaxis("日本确诊人数",y_date2)
line.add_yaxis("印度确诊人数",y_date3)
#设置全局配置项set_global_opts
line.set_global_opts(title_opts=TitleOpts(title="美日印三国确诊病例数",pos_left="center",pos_bottom="90%"),
                     legend_opts=LegendOpts(is_show=True),
                     toolbox_opts=ToolboxOpts(is_show=True),
                     )
#生成图像
line.render("数据处理与绘图.html")
#关闭文件
f_us.close()
f_jp.close()
f_id.close()














