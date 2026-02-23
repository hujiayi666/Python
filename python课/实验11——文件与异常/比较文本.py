"""编写一个函数compare（file1,file2），比较两个文本文件内容是否相同，如果内容相同返回True, 否则返回False。
在主程序中输入两个要比较的两文件名，然后调用以上函数进行比较。
如果文件内容相同则输出“No difference!”;
如果文件内容不相同，输出从第几个字符开始不相同。"""
def compare(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        return True
    else:
        min_len = min(len(content1), len(content2))
        for i in range(min_len):
            if content1[i]!= content2[i]:
                return i + 1
        return min_len + 1

if __name__ == "__main__":
    file1_name = input("请输入第一个文件名：")
    file2_name = input("请输入第二个文件名：")

    result = compare(file1_name, file2_name)
    if result is True:
        print("No difference!")
    else:
        print(f"从第{result}个字符开始不相同。")













