import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 8080))
server.listen(5)

print("HTTP server listening on port 8080")

conn, addr = server.accept()

print(f"Connected: {addr}")

data = conn.recv(4096)

print("----- HTTP REQUEST -----")
print(data.decode("utf-8"))

message = "Hello from my Python HTTP server!"

response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    f"Content-Length: {len(message.encode('utf-8'))}\r\n"
    "Connection: close\r\n"
    "\r\n"
    + message
)

conn.sendall(response.encode("utf-8"))

conn.close()
server.close()