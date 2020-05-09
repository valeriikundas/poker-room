import json
import logging
import os
import sys
import time

import pika
from pika.exceptions import AMQPConnectionError

# TODO:fix and remove
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if True:
    from gameplay.hand import Hand


def callback(ch, method, properties, body):
    logging.info(f" [x] Start hand: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print(body)
    data = json.loads(body)
    Hand(data).run()

    logging.info(" [x] Hand finished")


def connect(rabbitmq_url):
    while True:
        try:
            connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
            channel = connection.channel()
            logging.info("rabbitmq connected")
            return connection, channel
        except AMQPConnectionError:
            logging.error("waiting for RabbitMQ to become available...")
            time.sleep(3)


def main():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    RABBITMQ_URL = os.environ.get(
        "RABBITMQ_URL", "amqp://user:password@localhost:5672/%2F"
    )

    connection, channel = connect(RABBITMQ_URL)

    channel.exchange_declare(exchange="start_hand_queue", exchange_type="fanout")

    result = channel.queue_declare(queue="start_hand_queue", durable=True)
    queue_name = result.method.queue

    channel.queue_bind(queue=queue_name, exchange="start_hand_queue")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    logging.info(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
