import os
import sys
import logging
import pika

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.messaging.inbound import process_message as process_inbound_message
from src.messaging.outbound import process_message as process_outbound_message
from src.config import RABBITMQ_HOST, INBOUND_QUEUE, OUTBOUND_QUEUE

logger = logging.getLogger(__name__)

# Define the RabbitMQ connection parameters
params = pika.ConnectionParameters(host=RABBITMQ_HOST)

# Connect to RabbitMQ and set up the inbound and outbound queues
connection = pika.BlockingConnection(params)
inbound_channel = connection.channel()
inbound_channel.queue_declare(queue=INBOUND_QUEUE)
outbound_channel = connection.channel()
outbound_channel.queue_declare(queue=OUTBOUND_QUEUE)


# Set up a consumer for the inbound queue
def on_message_callback(_channel, _method, _properties, message_body):
    logger.debug("Received message: %s", message_body)
    inbound_result = process_inbound_message(message_body)
    outbound_result = process_outbound_message(inbound_result)
    logger.debug("Processed message: %s", outbound_result)
    outbound_channel.basic_publish(exchange="", routing_key=OUTBOUND_QUEUE, body=outbound_result)


# Set up a consumer for the inbound queue
inbound_channel.basic_consume(
    queue=INBOUND_QUEUE, on_message_callback=on_message_callback
)

# Start consuming messages from the inbound queue
logger.debug("Start consuming messages from the inbound queue")
inbound_channel.start_consuming()
