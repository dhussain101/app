from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError
from elasticsearch import Elasticsearch
import json
import time


def es_add(new_lottery, es_hook, es_index):
    # FIX: for now use 'title' as the id, but I think this should use the serializer's id instead so that
    # titles don't have to be unique. This would require the id data to be returned by the post request
    # in the exp layer after the new lottery has been assigned a unique id in the model layer
    es_hook.index(index=es_index, doc_type='listing', id=new_lottery['title'], body=new_lottery)
    es_hook.indices.refresh(index=es_index)


def listen(es_hook, kafka_hook):
    for message in kafka_hook:
        # add each new addition to ES
        new_lottery = json.loads(message.value.decode('utf-8'))
        es_add(new_lottery, es_hook, 'lottery_index')


def try_connect():
    while True:
        try:
            consumer = KafkaConsumer('lotteries', group_id='lottery-indexer', bootstrap_servers=['kafka:9092'])
            es = Elasticsearch(['es'])
            break
        except NodeNotReadyError:
            time.sleep(3)
    listen(es, consumer)


try_connect()
