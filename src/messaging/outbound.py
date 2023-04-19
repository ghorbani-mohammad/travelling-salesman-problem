import logging

logger = logging.getLogger(__name__)


def process_message(body):
    # Receive message from outbound queue

    # Do possible processing?
    # ...
    tour = body

    logger.debug("Optimized Tour: %s", tour)

    return body
