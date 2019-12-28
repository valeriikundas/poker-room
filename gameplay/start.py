"""[summary]

start listens for start hand requests and starts them
"""

import json
import logging
import os
import sys
import time

import environ
import pika
from pika.exceptions import AMQPConnectionError

# TODO:fix and remove
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if True:
    from gameplay.hand import Hand


def callback(ch, method, properties, body):
    logging.info(f" [x] Start hand: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

    data = json.loads(body)
    Hand(data).run()

    logging.info(" [x] Hand finished")


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

env = environ.Env()
environ.Env.read_env()

RABBITMQ_URL = env("RABBITMQ_URL")

connection = None
channel = None

while True:
    try:
        connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        channel = connection.channel()
        logging.info("rabbitmq connected")
        break
    except AMQPConnectionError:
        logging.error("waiting for RabbitMQ to become available...")
        time.sleep(3)

channel.exchange_declare(exchange="start_hand", exchange_type="fanout")

result = channel.queue_declare(queue="start_hand_queue", durable=True)
queue_name = result.method.queue

channel.queue_bind(queue=queue_name, exchange="start_hand")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=callback)

logging.info(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
