Remove the Disconnected Clients
=================

In this activity, you will learn to remove the clients from the list that are not connected to the server.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10858911/pasted-from-clipboard.png" height = "281" >

Follow the given steps to complete this activity:


* Open the file `server.py`.


* Define a remove function that takes a connection parameter and access clients as global.
~~~python
def remove(connection):
    global clients
~~~


* Check if the specified connection is present in the clients list.
~~~python
if connection in clients:
~~~


* Remove the specified connection from the clients list and print the message indicating that the client has been removed.
~~~python
clients.remove(connection)
print("Removed Client")
~~~


* Comment the error message in the expect block and call the remove function with the current client.
~~~python
 # print('Error while sending to', connection)
 remove(client)
~~~


* Save and run the code to check the output.
