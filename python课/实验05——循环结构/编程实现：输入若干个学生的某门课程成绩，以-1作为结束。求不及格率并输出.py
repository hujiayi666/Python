"""编程实现：输入若干个学生的某门课程成绩，以-1作为结束。求不及格率并输出"""
# 初始化计数器
count = 0  # 用于统计学生总数
fail_count = 0  # 用于统计不及格的学生数
# 输入成绩
score = float(input("请输入学生成绩（输入 -1 结束）: "))
while score!= -1:
    count += 1  # 每输入一个成绩，学生总数加 1
    if score < 60:  # 如果成绩小于 60 ，则为不及格
        fail_count += 1  # 不及格学生数加 1
    score = float(input("请输入学生成绩（输入 -1 结束）: "))
# 计算不及格率
fail_rate = fail_count / count * 100  # 不及格率 = 不及格人数 / 总人数 * 100
# 输出不及格率
print("不及格率为：{:.2f}%".format(fail_rate))
