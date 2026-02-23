"""小明参加了语文、数学和英语三门课程考试，需要编写一个 Python 程序实现以下功能：
计算三门课程考试成绩的总和。
计算三门课程考试成绩的平均值。
找出三门课程考试成绩中的最高分和最低分。
如果三门课程考试成绩分别以权重 0.5、0.3 和 0.2 计入总评成绩，计算小明的最终总评成绩。"""
chinese=int(input("小明的语文成绩为:"))
mathematics=int(input("小明的数学成绩为:"))
english=int(input("小明的英语成绩为:"))
a=chinese+mathematics+english
print(f"三门课程考试成绩的总和为:{a}")
average=a/3
print(f"三门课程考试成绩的平均值为{average}")
b=max(chinese,mathematics,english)
c=min(chinese,mathematics,english)
print(f"三门课程考试成绩中的最高分为{b}最低分为{c}")
total_grate=chinese*0.5+mathematics*0.3+english*0.2
print(f"小明的最终总评成绩为{total_grate}")






