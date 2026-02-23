#导包
import socket
#创建Socket对象
socket_sever=socket.socket()
#绑定id和端口
socket_sever.bind(("localhost",8888))
#监听端口
socket_sever.listen(1)
#等待客户端连接
result=socket_sever.accept()
conn=result[0]     #客户端和服务器的链接对象
address=result[1]  #客户端的地址信息

print(f"接受到了客户端的连接，客户端的信息是{address}")
while True:
#接收客户端信息，要使用客户端和服务端的本次链接对象，而不是socket_server对象
    data=conn.recv(1024).decode("UTF-8")
    #接受消息
    print(f"客户端发来的消息是{data}")
    #发送消息
    msg=input("请输入你要和客户端回复的消息：")         #encode可以将字符串编码为数组对象
    if msg=="退出":
        break
    conn.send(msg.encode("UTF-8"))

#关闭链接
conn.close()
socket_sever.close()


































