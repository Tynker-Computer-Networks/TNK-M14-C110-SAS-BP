import socket
# Import Thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

clients = []

print("Server has started...")

# Define clientThread method


    # Create an infinite loop
    
        # Create a try block
        
            # Receive the message on the connection i.e. "conn" and store it in message variable
            
            # Check if message exits
            
                # Print the message
                
        # Create except block
        
            # Continue the loop 
            

while True:
    conn, addr = server.accept()
    
    print("New Client Connected", addr[0])
    clients.append(conn)

    # Move this line to the clientThread method
    conn.send("Welcome to this chatroom!".encode())
    
    # Create a new thread with clientThread as target and conn, addr as args
    
    # start the new thread
    
