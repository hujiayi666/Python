from pymysql import Connection #导包
#构建mysql数据库连接
conn=Connection(
    host="localhost",   #主机名（ip)
    port=3306,          #端口
    user="root",        #账号
    password="HJY200538hjy",#密码
    autocommit=True      #自动插入
)
#获取游标对象
coursor=conn.cursor()
conn.select_db("world")  #选择数据库
#使用游标对象，执行sql语句
#coursor.execute("create table test_pymysql(id int);")
#执行查询性质的sql
coursor.execute("insert into student values (10001,'周杰伦',31,'男')")
coursor.execute("insert into student values (10002,'林俊杰',33,'男')")
#通过commit确认
conn.close()












