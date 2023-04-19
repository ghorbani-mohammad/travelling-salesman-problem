import os
import sys
import pika
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.config import RABBITMQ_HOST, INBOUND_QUEUE, OUTBOUND_QUEUE

# Define the RabbitMQ connection parameters
params = pika.ConnectionParameters(host=RABBITMQ_HOST)

# Connect to RabbitMQ and set up the inbound and outbound queues
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=INBOUND_QUEUE)
channel.queue_declare(queue=OUTBOUND_QUEUE)

# Prepare the message payload
locations_string = sys.argv[1]
locations = json.loads(locations_string)
payload = {"locations": locations}
message = json.dumps(payload)

# Publish the message to the inbound queue
channel.basic_publish(exchange="", routing_key=INBOUND_QUEUE, body=message)

# Define the callback function for consuming messages
def callback(ch, method, properties, body):
    print("Received message:", body.decode())

# Start consuming messages from the output queue
channel.basic_consume(queue=OUTBOUND_QUEUE, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

# Close the connection
connection.close()