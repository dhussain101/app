from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError
from elasticsearch.exceptions import ConnectionError
from elasticsearch import Elasticsearch
import json
import time
import socket
import sys


def es_add(new_lottery, es_hook, es_index):
    # FIX: for now use 'title' as the id, but I think this should use the serializer's id instead so that
    # titles don't have to be unique. This would require the id data to be returned by the post request
    # in the exp layer after the new lottery has been assigned a unique id in the model layer
    es_hook.index(index=es_index, doc_type='listing', id=new_lottery['title'], body=new_lottery)
    es_hook.indices.refresh(index=es_index)


def load_fixtures(es_hook):
    with open('../data/db.json', 'r') as db:
        data = json.loads(db.read())
    for data_row in data:
        if data_row['model'] == 'models_app.lottery':
            es_add(data_row['fields'], es_hook, 'lottery_index')


def listen(es_hook, kafka_hook):
    for message in kafka_hook:
        # add each new addition to ES
        new_lottery = json.loads(message.value.decode('utf-8'))
        es_add(new_lottery, es_hook, 'lottery_index')


def try_connect():
    # use socket to attempt to connect to es
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(sys.argv[1]), 9200))
        if result == 0:
            break
        else:
            time.sleep(3)

    # we should be connected by now
    es = Elasticsearch(['es'])

    # using try/catch seems to work better for kafka, as it dies/restarts
    # which can trick the socket check into thinking it's on when
    # in reality it just turned back off
    while True:
        try:
            consumer = KafkaConsumer('lotteries', group_id='lottery-indexer', bootstrap_servers=['kafka:9092'])
            break
        except NodeNotReadyError:
            time.sleep(3)

    load_fixtures(es)
    listen(es, consumer)


try_connect()
