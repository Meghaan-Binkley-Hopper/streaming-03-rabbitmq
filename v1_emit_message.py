"""
    This program sends a message to a queue on the RabbitMQ server.

    Meghaan Binkley-Hopper
    Date: January 30, 2023

"""

# add imports at the beginning of the file
import pika #Installed pika in order for the import to work.

message = 'hello world.' #Declaring message variable in order to make reuseable.

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message) #added message variable
#Change 1: My name is Meghaan.
#Change 2: Message #2.
#Change 3: Last new message.
# print a message to the console for the user
print(" [x] Sent ", message) #added message variable
# close the connection to the server
conn.close()
