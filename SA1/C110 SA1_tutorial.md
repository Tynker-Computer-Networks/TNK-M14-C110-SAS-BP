Add Multiple Clients to the Server
============================

In this activity, you will learn to name the client by creating a thread for each client and then connecting them to the server.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10858624/C110_SA1.gif" width = "521" height = "281">
​

Follow the given steps to complete this activity:


1. Assign a name to the client
* Open the `client.py` file.


* Get a nickname from console input and store it in the variable nickname.
~~~python
nickname = input("Choose your nickname: ")
~~~


* Get a nickname into the message variable.
~~~python
message = nickname: 
~~~


* Send the message over a network connection using a client object. Before sending it, encode the message to bytes using the UTF-8 encoding. 
~~~python
client.send(message.encode('utf-8'))
~~~

2. Define a thread to assign a name to the client

* Open the `server.py` file.


* Imports the Thread class specifically from the threading module. To create and manage threads in a multithreaded program
~~~python
from threading import Thread
~~~


* Define a function called clientThread that takes two parameters, conn and addr. 
conn represents a network connection to a client, 
addr typically contains information about the client's address.
~~~python
def clientThread(conn, addr)
~~~


* Send a welcome message to the connected client. After encoding it in UTF-8 format to ensure it's transmitted as bytes.
~~~python
conn.send("Welcome to this chatroom!".encode('utf-8'))
~~~


* Create an infinite loop and continue to run until it is explicitly terminated from within or from an external source.
~~~python
while True:
~~~


* Create a try block and receive the message on the connection i.e. "conn" and store it in the message variable. 
~~~python
 try:
       message = conn.recv(2048).decode('utf-8')
~~~


* Check if the message has a value. If a message is received, print the message to the console
~~~python
if message:
       print("Message from client: ", message)
~~~


* Create except block and continue the loop to keep the server running even if there are errors in receiving or processing messages
~~~python
except:
       continue
~~~


3. Move the piece of code to notify the client
* Move the following line of code to the clientThread method and add # to comment it here. 
~~~python
# conn.send("Welcome to this chatroom!".encode())
~~~


4. Append the new clients
* Create a new thread with clientThread as target and conn, addr as args
clientThread, which is a function defined elsewhere in the code. This function is responsible for handling the client's communication.
conn, which represents the network connection to the client, and addr, which typically contains information about the client's address.
~~~python
new_thread = Thread(target=clientThread, args=(conn, addr))
~~~


5. Create and start a thread
* Start the new thread to handle multiple client connections concurrently, allowing the server to serve multiple clients at the same time.
~~~python
new_thread.start()
~~~


* Save and run the code to check the output. Let's name and connect the client to the server.
