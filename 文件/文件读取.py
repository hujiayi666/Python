#打开文件，以读取模式打开
f=open("D:/hujiayi.txt.txt","r",encoding="UTF-8")
#方式1，读取全部内容，通过count法统计itheima的个数
i=f.read()
count=i.count("itheima")
print(f"itheima在文件中出现了{count}次")
#关闭文件
f.close()





