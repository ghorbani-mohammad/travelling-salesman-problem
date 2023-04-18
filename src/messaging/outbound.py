import pika

from src.config import RABBITMQ_HOST, OUTBOUND_QUEUE

# Define the RabbitMQ connection parameters
params = pika.ConnectionParameters(host=RABBITMQ_HOST)

# Connect to RabbitMQ and set up the inbound and outbound queues
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue=OUTBOUND_QUEUE)


def callback(_ch, method, _properties, body):
    # Receive message from outbound queue
    tour = body.decode()

    # Print the tour
    print("Optimized Tour:", tour)

    # Acknowledge message received
    channel.basic_ack(delivery_tag=method.delivery_tag)


# Start consuming from outbound queue
channel.basic_consume(queue=OUTBOUND_QUEUE, on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()
