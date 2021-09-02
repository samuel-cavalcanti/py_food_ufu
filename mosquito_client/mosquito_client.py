import dataclasses

import paho.mqtt.client as mosquito_client
from paho.mqtt.client import MQTTMessage
from client_crud import Client
import json
from enum import Enum


class Topic(Enum):
    ADDED_CLIENTS = 'clients/add_clients'
    REMOVED_CLIENTS = 'clients/rm_clients'


class MosquittoClient:
    __topic = 'clients'
    __added_clients_topic = 'add_clients'
    __removed_clients_topic = 'rm_clients'

    def __init__(self):
        self.__client = mosquito_client.Client()
        self.__client.connect(host='localhost')
        self.__client.on_message(self.__on_message)
        self.__subscribers = {self.__added_clients_topic: [], self.__removed_clients_topic: []}

    def publish_client(self, client: Client, topic: Topic):
        client_json = json.dumps(dataclasses.asdict(client))
        self.__client.publish(topic.value, client_json)

    def subscribe_in_topic(self, callback, topic: Topic):
        self.__client.subscribe(topic.value)
        self.__subscribers[topic.value].append(callback)

    def __on_message(self, client, userdata, message: MQTTMessage):
        for callback in self.__subscribers[message.topic]:
            callback(message.payload.decode())
