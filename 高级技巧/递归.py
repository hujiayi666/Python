import os

def test_os():
    print(os.listdir("D:/360Downloads"))                   #列出路径下的内容
    #print(os.path.isdir("D:/360Downloads/pythonProject"))  #判断指定路径是不是文件夹
    #print(os.path.exists("D:/360Downloads"))               #判断指定路径是否存在


def get_files_resource_from_dir(path):
    file_list=[]
    if os.path.exists(path):
        for f in os.listdir(path):
            new_pass=path+"/"+f
            if os.path.isdir(new_pass):
                get_files_resource_from_dir(new_pass)
            else:
                file_list.append(new_pass)
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list

if __name__=='__main__':
    print(get_files_resource_from_dir("D:/360Downloads"))
















