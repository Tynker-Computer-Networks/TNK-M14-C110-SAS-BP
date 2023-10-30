Send Messages from Client to Server
===========================

In this activity, you will learn to send messages from multiple clients to the server by creating threads to write input messages.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10858663/C110_SA2.gif" width = "521" height = "281">


Follow the given steps to complete this activity:


1. Store the input message
* Open the `client.py` file.


* Imports the Thread class specifically from the threading module.
~~~python
from threading import Thread
~~~


* Create the write() function, then create an infinite loop using a while statement with the condition True. So that the code inside the loop will keep running indefinitely until explicitly terminated from an external source.
~~~python
def write():
    while True:
~~~


* Inside the loop, construct a message by formatting the nickname and the user's input.
~~~python
message = '{}: {}'.format(nickname, input(''))
~~~


2. Send the encoded client message
* Send the constructed message to a remote entity using a client object. Encode the message in UTF-8 format to convert it from a Unicode string to bytes, which is suitable for network transmission.
~~~python
client.send(message.encode('utf-8'))
~~~


3. Create and start a thread to write messages

* Create a new thread object named write_thread using the Thread constructor. Set the target parameter to write.
~~~python
write_thread = Thread(target=write)
~~~


* Start the thread by invoking the start() method on the write_thread object to execute the write function in parallel with the main program or other threads.
~~~python
write_thread.start()
~~~


* Save and run the code to check the output.
