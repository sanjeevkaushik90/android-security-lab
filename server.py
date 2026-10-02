import socket
import threading


port = 8080

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, port)

print(f"server is starting..... on {port}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)


def handle_client(conn, addr):
    with conn:
        print(f"Connected successfully by client at: {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                break

            print(data.decode("utf-8"))

            message="Message received"

            conn.sendall(message.encode("utf-8"))


while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    thread.start()

