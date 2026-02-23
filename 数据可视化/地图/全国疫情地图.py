#全国疫情地图绘制

#导包
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts.options import TitleOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import LegendOpts
#读取文件
f=open("D:/疫情.txt","r",encoding="UTF-8")
data=f.read()
f.close()   #关闭文件
#将文件转换为字典模式
data_dict=json.loads(data)
#从字典中取出各省数据
data_dict_province=data_dict["areaTree"][0]["children"]
#组装每个省份和确诊人数为元组，并各个省的数据都封装到列表中
data_list=[]      #定义一个列表
for data_province in data_dict_province:
    name_province=data_province["name"]
    confirm_province=data_province["total"]["confirm"]
    data_list.append((name_province,confirm_province))
#建立一个地图
map=Map()
#添加数据
map.add("各省份确诊人数",data_list,"china")
#设置全局配置，定制分段视觉映射
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[{"min":1,"max":99,"lable":"1-99人","color":"#CCFFFF"},
                {"min":100,"max":999,"lable":"100-999人","color":"#FFFF99"},
                {"min":1000,"max":4999,"lable":"1000-4999人","color":"#FFF9966"},
                {"min":5000,"max":9999,"lable":"5000-9999人","color":"#FF6666"},
                {"min":10000,"max":99999,"lable":"10000-99999人","color":"#CC3333"},
                {"min":100000,"max":999999,"lable":"100000-999999人","color":"#990033"}
        ]
    ),
    title_opts=TitleOpts(title="全国疫情地图",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)
#生成图像
map.render("全国疫情地图.html")














