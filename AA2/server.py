import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []

print("Server has started...")

# Debug why message is not sent to all the clients
def clientThread(conn, addr):
    conn.send("Welcome to this chatroom!".encode('utf-8'))

    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print(message)
                
        except:
            continue

def broadcast(message, connection):
    # Make sure we are updating the global clients list
    
    for client in clients:
        if client!=connection:
            try:
                print("Sending to client")
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(connection):
    global clients
    if connection in clients:
        clients.remove(connection)
        print("Removed Client")

while True:
    conn, addr = server.accept()
    
    print("New Client Connected", addr[0])
    clients.append(conn)
    
    new_thread = Thread(target= clientThread,args=(conn, addr))
    new_thread.start()
