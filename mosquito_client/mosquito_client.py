import dataclasses

import paho.mqtt.client as mosquito_client
import paho.mqtt.subscribe as subscribe
import json


class MosquittoClient:
    def __init__(self):
        self.__client = mosquito_client.Client()
        self.__client.connect(host='localhost')
        self.__topic = 'clients'

    def publish_client(self, client):
        client_json = json.dumps(dataclasses.asdict(client))
        self.__client.publish(self.__topic, client_json)

    @staticmethod
    def subscribe_in_clients(function):
        subscribe.callback(function, 'clients')
