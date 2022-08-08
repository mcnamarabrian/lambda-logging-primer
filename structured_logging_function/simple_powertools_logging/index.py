import random

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


@logger.inject_lambda_context
def handler(event: dict, context: LambdaContext) -> str:
    logger.info({'Random number':random.randrange(100) + 1})
