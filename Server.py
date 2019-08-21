"""
Create a server for chatting with client
"""
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 6543
BUFFER_SIZE = 1024
first_answer = b"Hello, client! I am a server. How are you?"
second_answer = b"Thanks! Good bye!"
cnt = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print("Connected by", address)
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            if cnt == 0:
                conn.send(first_answer)
                cnt += 1
            elif cnt == 1:
                conn.send(second_answer)
                cnt += 1
            else:
                break
print("Close connection")
