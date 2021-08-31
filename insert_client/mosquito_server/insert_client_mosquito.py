import dataclasses

import paho.mqtt.client as mosquito_client
import json


class MosquittoClient:
    def __init__(self):
        self.__client = mosquito_client.Client()
        self.__client.connect(host='localhost')
        self.__topic = 'clients'

    def publish_client(self, client):
        client_json = json.dumps(dataclasses.asdict(client))
        print(f"client:{client} json:{client_json}")
        self.__client.publish(self.__topic, client_json)
