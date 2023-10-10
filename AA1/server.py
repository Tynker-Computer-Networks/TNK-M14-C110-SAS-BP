import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []

print("Server has started...")

def clientThread(conn, addr):
    conn.send("Welcome to this chatroom!".encode('utf-8'))

    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print(message)
                broadcast(message, conn)
        except:
            continue

def broadcast(message, connection):
    global clients
    for client in clients:
        if client!=connection:
            try:
                print("Sending to client")
                client.send(message.encode('utf-8'))
            except:
                # Comment this line
                print('Error while sending to', connection)
                # Call remove function with current client
                

# Define a remove function that takes connection parameter

    # Access clients as global
    
    # Check if connection exits in clients
    
        # Remove the connection from clients
        
        # Print Removed Client
        

while True:
    conn, addr = server.accept()
    
    print("New Client Connected", addr[0])
    clients.append(conn)
    
    new_thread = Thread(target= clientThread,args=(conn, addr))
    new_thread.start()
