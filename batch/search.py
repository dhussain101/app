from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json


def es_add(listing, es, es_index):
    # FIX: for now use 'title' as the id, but I think this should use the serializer's id instead so that
    # titles don't have to be unique. This would require the id data to be returned by the post request
    # in the exp layer after the new lottery has been assigned a unique id in the model layer
    es.index(index=es_index, doc_type='listing', id=new_lottery['title'], body=listing)
    es.indices.refresh(index=es_index)


# create a consumer to listen for additions to the lotteries queue
consumer = KafkaConsumer('lotteries', group_id='lottery-indexer', bootstrap_servers=['kafka:9092'])
es = Elasticsearch(['es'])

for message in consumer:
    # add each new addition to ES
    new_lottery = json.loads(message.value.decode('utf-8'))
    es_add(new_lottery, es, 'lottery_index')
