import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
nickname = input("Choose your nickname: ")

client.connect((ip_address, port))
print("Connected with the server...")

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break
        

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()


write_thread = Thread(target=write)
write_thread.start()