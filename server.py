import socket
import threading

port = 8080
SERVER= socket.gethostbyname(socket.gethostname())
ADDr=(SERVER,port)

print(f"server is starting..... on {port}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDr)
server.listen(5)


conn,addr=server.accept()

with conn:
        print(f"Connected successfully by client at: {addr}")
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                break
            conn.sendall(data) 

