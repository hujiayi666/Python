#导包
import pyecharts
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
#通过Line()来创建一个折线图对象
line1=pyecharts.charts.Line()
#给折线图添加x轴对象的数据
line1.add_xaxis(["中国","美国","英国"])
#给y轴对象添加数据
line1.add_yaxis("GDP",[16,26,4])
#设置全局配置项set_global_opts
line1.set_global_opts(title_opts=TitleOpts(title="中美英三国GDP",pos_left="center",pos_bottom="1%"),#标题,pos_left控制左右
#pos_bottom控制上下
                     legend_opts=LegendOpts(is_show=True),#
                     toolbox_opts=ToolboxOpts(is_show=True),
                     visualmap_opts=VisualMapOpts(is_show=True))
#通关render查看
line1.render("GDP图.html")






