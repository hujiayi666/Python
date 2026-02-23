#打开文件，读取数据
f=open("D:/bill.txt.txt","r",encoding="UTF-8")
#建立一个新文件
f1=open("D:/bill.txt.bak","w",encoding="UTF-8")
#通过for循环来取得数据
for line in f:
    #通过strip来去掉分行
    line=line.strip()
    #if判断是否为“测试”
    if line.split("，")[4]=="测试":#加split来去掉逗号，变成列表，通过下标索引来取到目标值
        continue#countinue循环，跳过这一环节
    else:
        f1.write(line)#将line写入新文件
        f1.write("\n")#通过\n来换行
f.close()
f1.close()



















