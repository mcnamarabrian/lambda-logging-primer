import random

def handler(event, context):
    print(f'Random number: {random.randrange(100) + 1}')

