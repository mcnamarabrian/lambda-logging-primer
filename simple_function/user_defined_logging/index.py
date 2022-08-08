import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(f'Generated random number {random.randrange(100) + 1}')
