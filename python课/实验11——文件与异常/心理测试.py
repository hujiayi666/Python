import re
import os
def calculate_students_scores(answer_file, result_file, score_file):
    # 读取答案文件，将答案和分数存储为字典
    answer_dict = {}
    with open(answer_file, 'r') as afile:
        for line in afile.readlines():
            line = line.strip()
            question_num = int(re.search(r'\d+', line).group())
            answer_dict[question_num] = line[re.search(r'\d+', line).end():]
    # 读取考生答案文件，计算每个考生的成绩
    student_scores = {}
    with open(result_file, 'r') as rfile:
        for line in rfile.readlines():
            line = line.strip()
            student_id, student_answer = line.split(':')
            score = 0
            for i, char in enumerate(student_answer):
                question_num = i + 1
                option_scores = answer_dict[question_num].split(char)[1]
                score_value = int(re.search(r'\d+', option_scores).group())
                score += score_value
            student_scores[student_id] = score

    # 将考生成绩写入新文件
    with open(score_file, 'w') as sfile:
        for student_id, score in student_scores.items():
            sfile.write(f"{student_id}的得分: {score}分\n")

if __name__ == "__main__":
    answer_file =r"C:\python\answer.txt"
    result_file =r"C:\python\result.txt"
    score_file = "score.txt"
    print("当前工作目录：", os.getcwd())

    calculate_students_scores(answer_file, result_file, score_file)













