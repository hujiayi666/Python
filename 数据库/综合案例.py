from file_define import TextFileReader,JsonFileReader
from data_define import Record
from pymysql import Connection
text_file_reader=TextFileReader("D:/2011年1月销售数据(1).txt")
json_file_reader=JsonFileReader("D:/2011年2月销售数据JSON(1).txt")

jan_data:list[Record]=text_file_reader.read_data()
feb_data:list[Record]=json_file_reader.read_data()

all_data:list[Record]=jan_data + feb_data
print(all_data)
#构建mysql链接对象
conn=Connection(
    host="localhost",   #主机名（ip)
    port=3306,          #端口
    user="root",        #账号
    password="HJY200538hjy",#密码
    autocommit=True      #自动插入
)
#获得游标对象
cursor=conn.cursor()
#选择数据库
conn.select_db("py_sql")
#组织sql语句
for record in all_data:
    sql=f"insert into orders(order_date,order_id,money,province)"\
         f" values ('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    #执行sql语句
    cursor.execute(sql)
conn.close()






