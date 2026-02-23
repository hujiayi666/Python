from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map=Map()
data=[
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("湖北省",399),
    ("台湾省",499),
    ("河北省",599),
    ("河南省",699),
    ("广东省",799),
    ("天津市",206),
    ("江西省",132),
    ("江苏省",657)
]
map.add("测试地图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[{"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
                {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
                {"min":100,"max":499,"label":"100-499","color":"#990033"},
                {"min":500,"max":800,"label":"500-800","color":"blue"},]
    )



)
map.render()












