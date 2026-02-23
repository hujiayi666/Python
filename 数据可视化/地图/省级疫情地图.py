#安徽省疫情地图绘制

#导包
import  json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts.options import TitleOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import LegendOpts
#读取文件
f_anhui=open("D:/疫情.txt","r",encoding="UTF-8")
data=f_anhui.read()
f_anhui.close()#关闭文件
#将文件转换为字典模式
data_dict=json.loads(data)
#从字典中取出安徽省数据
data_dict_anhui=data_dict["areaTree"][0]["children"][31]["children"]
#组装每个省份和确诊人数为元组，并各个省的数据都封装到列表中
data_list=[]        #定义一个列表
for data_anhui in data_dict_anhui:
    name_cities=data_anhui["name"]+"市"
    confirm_cities=data_anhui["total"]["confirm"]
    data_list.append((name_cities,confirm_cities))
#建立一个地图
map=Map()
#添加数据
map.add("安徽省疫情分布图",data_list,"安徽")
#设置全局配置，定制分段视觉映射
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[{"min":1,"max":49,"lable":"1-49人","color":"#CCFFFF"},
                {"min":50,"max":99,"lable":"50-99人","color":"#FFFF99"},
                {"min":100,"max":199,"lable":"100-199人","color":"#FFF9966"},
                {"min":200,"max":499,"lable":"200-499人","color":"#FF6666"},
                {"min":500,"max":999,"lable":"500-999人","color":"#CC3333"},
                {"min":1000,"max":2999,"lable":"1000-2999人","color":"#990033"}
        ]
    ),
    title_opts=TitleOpts(title="安徽省疫情地图",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)
#生成图像
map.render("安徽省疫情地图.html")








