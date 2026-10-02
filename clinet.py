import socket

port=8080
client=socket.gethostbyname(socket.gethostname())
ADDr=(client,port)

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT.connect(ADDr)

data=input()
CLIENT.sendall(data.encode('utf-8'))

response = CLIENT.recv(1024)
print(response.decode("utf-8"))

CLIENT.close()