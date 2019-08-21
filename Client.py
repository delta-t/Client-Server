"""
Create a simple chat with server. If server is not responding - terminate the connection and report about error.
Otherwise, print the chat and then close the connection.

"""
import socket


def chat_with_server(ip, port, buffer):
    first_message = b"Hello, server! I am a client."
    second_message = b"I'm fine. Nice to connect to you!"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((ip, port))
        except ConnectionRefusedError:
            print("Sorry, server is not responding")
            return

        s.send(first_message)
        print("Client:", first_message.decode("utf-8"))

        first_answer = s.recv(buffer)
        print("Server:", first_answer.decode("utf-8"))

        s.send(second_message)
        print("Client:", second_message.decode("utf-8"))

        second_answer = s.recv(buffer)
        print("Server:", second_answer.decode("utf-8"))


if __name__ == '__main__':
    TCP_IP = '127.0.0.1'
    TCP_PORT = 6543
    BUFFER_SIZE = 1024
    chat_with_server(ip=TCP_IP, buffer=BUFFER_SIZE, port=TCP_PORT)
