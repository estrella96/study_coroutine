#server
import socket

def serverFunc():
    #socket.AF_INETL:使用ipv4
    #socket.SOCK_DGRAM:使用UDP通信
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr=("127.0.0.1",7852)
    sock.bind(addr)
    data,addr=sock.recvfrom(500)
    print(data)
    print(type(data))
    #发送的数据需要解码
    text=data.decode()
    print(text)
    print(type(text))

    #返回信息
    rsp="It is Pok"
    data=rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    print("start")
    serverFunc()
    print("end")

