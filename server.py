import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 80))
server_socket.listen(1)

print("Server is running")

while True:
    conn, addr = server_socket.accept()
    try:
        message = conn.recv(1024)
        filename = message.split()[1].decode("UTF-8").strip("/")
        print(filename)

        f = open(filename)
        outputdata = f.read()
        print(outputdata)
        f.close()

        conn.send("HTTP/1.0 200 OK\r\n\r\n".encode())
        for i in range(0, len(outputdata)):
            conn.send(outputdata[i].encode())
        conn.close()

        print("Successfully sended")
    except IOError:
        conn.send("404 Not Found".encode())
        conn.close()

        print("Error sended")

server_socket.close()
