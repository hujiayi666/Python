#导包
import socket
#创建socket对象
socket_client=socket.socket()
#绑定id和端口
socket_client.connect(("localhost",8888))
while True:
    #发送消息
    msg=input("请输入你要给客户端发送的消息:")
    if msg=="退出":
        break      #结束聊天

    socket_client.send(msg.encode("UTF-8"))    #利用encode编码
    #接受消息
    recv_data=socket_client.recv(1024)
    print(f"服务端回复的消息为：{recv_data.decode('UTF—8')}")  #利用decode编码
#关闭程序
socket_client.close()




































