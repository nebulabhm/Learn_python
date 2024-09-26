# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:tcp-sever
# @Author: nebulabhm
# @Date:   2021/5/24 13:57
# @Description: 
# ---------------------------------------
import  socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen()
print(' 服务器启动。。。 ')


# 等待客户端连接
conn, address = s.accept()
# 客户端连接成功
print(address)

# 从客户端接受数据
data = conn.recv(1024)
print(' 从客户端接收消息： {0}'.format(data.decode()))

# 给客户端发送数据
conn.send(' 你好 '.encode())

# 释放资源
conn.close()
s.close()

