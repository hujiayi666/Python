#导包
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
#构建基本图表
bar1=Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[15,26,3.8],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2=Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[16,28,4],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3=Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[18,30,4.3],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

bar4=Bar()
bar4.add_xaxis(["中国","美国","英国"])
bar4.add_yaxis("GDP",[20,31,4.5],label_opts=LabelOpts(position="right"))
bar4.reversal_axis()

#构建时间线对象
timeline=Timeline({"theme":ThemeType.LIGHT})
#在时间线中添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
timeline.add(bar4,"点4")
#自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
#绘图
timeline.render("时间线柱状图.html")

