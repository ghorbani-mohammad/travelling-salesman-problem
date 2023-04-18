import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
INBOUND_QUEUE = os.getenv("INBOUND_QUEUE")
OUTBOUND_QUEUE = os.getenv("OUTBOUND_QUEUE")
