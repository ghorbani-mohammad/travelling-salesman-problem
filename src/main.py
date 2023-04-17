import os
import sys
import pika

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.inbound import process_message


INBOUND_QUEUE = "tsp.inbound"
OUTBOUND_QUEUE = "tsp.outbound"

# Define the RabbitMQ connection parameters
params = pika.ConnectionParameters(host="rabbitmq")


# Connect to RabbitMQ and set up the inbound and outbound queues
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=INBOUND_QUEUE)
# channel.queue_declare(queue=OUTBOUND_QUEUE)

# Set up a consumer for the inbound queue
channel.basic_consume(queue=INBOUND_QUEUE, on_message_callback=process_message)

# Start consuming messages from the inbound queue
channel.start_consuming()
