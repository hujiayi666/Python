import turtle  #导包
#搭建画板
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("画爱心")
#选择颜色和速度并构建画笔
pen=turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.pensize(3)
pen.speed(2)
#指挥画笔
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90,200)
pen.left(120)
pen.circle(-90,200)
pen.forward(180)
pen.end_fill()
#隐藏画笔
pen.hideturtle()
#停止作画
turtle.done()









