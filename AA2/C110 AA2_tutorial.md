​
Debug the Code
==============


In this activity, you will learn to debug the code to enable the client to receive messages sent from other clients.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10858719/C110_SA3.gif" width = "521" height = "281">


Follow the given steps to complete this activity:


* Run the code to check the why message is not sent to all the clients. The code is intended to create a chatroom where messages sent by one client are broadcasted to all other clients. If messages are not being sent to all clients, there's unexpected behavior or a bug in the code that needs to be identified and fixed.


* Open the file `server.py`.


* In the broadcast function, to keep track of all connections across multiple functions, it's essential to use a global variable for clients list. Without the global declaration, each function would create its own local clients variable, and changes made within one function wouldn't be reflected in other functions, leading to incorrect behavior.


* Make sure we are updating the global clients list in the broadcast function.
~~~python
global clients
~~~
* Save and run the code to check the output.


