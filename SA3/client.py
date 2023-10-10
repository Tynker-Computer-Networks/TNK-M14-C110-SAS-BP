import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
nickname = input("Choose your nickname: ")

client.connect((ip_address, port))
print("Connected with the server...")

# Create a receive() function

    # Create an infinite loop
    
        # write try block
        
            # indent following lines to be part of the while loop
            
            # line already present in boiler
            
        # Add except 
        
            # Print An error occurred!
            
            # Close the client socket
            
            # Break the loop 
            
        

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

# Create a thread receive_thread that runs receive function

# Start the receive_thread



write_thread = Thread(target=write)
write_thread.start()