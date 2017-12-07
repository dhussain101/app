import json
import time
import os

from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError


def listen(kafka_hook):
    file_path = '/data/data/views.log'
    if not os.path.isfile(file_path):
        open(file_path, 'w').close()
    for message in kafka_hook:
        new_view = json.loads(message.value.decode('utf-8'))
        with open(file_path, 'a') as log:
            log.write("%s\t%s\n" % (new_view[0], new_view[1]))


def try_connect():
    while True:
        try:
            consumer = KafkaConsumer('new_view', group_id='indexer', bootstrap_servers=['kafka:9092'])
            break
        except NodeNotReadyError:
            time.sleep(3)

    listen(consumer)


try_connect()
