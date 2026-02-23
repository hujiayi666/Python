"""某心理测试题全部由单选题组成，每个题目有3个选项，不同选项得分不同（但每题分数都是在10分-99分之间），答案和分数保存在一个文件answer.txt中，格式为：
其中最左边的数字为题号，其后是该题各选项的分数。
从键盘输入某位考生答案，例如：
ABCCBABCAABACBCABCBC
编程计算并输出该考生的成绩。"""
import re
def calculate_score(answer_file, student_answer):
    score = 0
    with open(answer_file, 'r') as file:
        lines = file.readlines()

    for i, char in enumerate(student_answer):
        line = lines[i].strip()
        option_scores = line.split(char)[1]

        # 使用正则表达式匹配并提取出开头的数字部分作为分数值
        score_value = int(re.search(r'\d+', option_scores).group())
        score += score_value

    return score
if __name__ == "__main__":
    answer_file =r"C:\python\answer.txt"
    student_answer = input("请输入考生答案：")
    total_score = calculate_score(answer_file, student_answer)
    print(f"该考生的成绩为：{total_score}分")