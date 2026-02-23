"""有一个文本文件student.txt，其中包含了所有学生的学号，格式如下。
154772  154778  154784  154793  156273  ……
请编写一个函数，每次调用该函数，能从文件student.txt包含的所有学号中随机抽取一位学生的学号。
如果老师要随机从所有学生中点3位学生回答问题。（学号不重复）
主程序应该如何设计。"""
import random
def get_random_student_id():
    with open("C:\python\student.txt", "r") as file:
        student_ids = file.read().split()
    return random.choice(student_ids)

if __name__ == "__main__":
    selected_students = []
    num_to_select = 3

    for i in range(num_to_select):
        while True:
            random_student_id = get_random_student_id()
            if random_student_id not in selected_students:
                selected_students.append(random_student_id)
                break

    print("被选中回答问题的学生学号为：")
    for student_id in selected_students:
        print(student_id)