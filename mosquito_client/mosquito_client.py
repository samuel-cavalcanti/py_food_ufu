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

    def __init__(self):
        self.__client = mosquito_client.Client()
        self.__client.connect(host='localhost')
        self.__client.on_message = self.__on_message
        self.__subscribers = {Topic.ADDED_CLIENTS.value: [], Topic.REMOVED_CLIENTS.value: []}

    def publish_client(self, client: Client, topic: Topic):
        client_json = json.dumps(dataclasses.asdict(client))
        self.__client.publish(topic.value, client_json)

    def subscribe_in_topic(self, callback, topic: Topic):
        self.__client.subscribe(topic.value)
        self.__subscribers[topic.value].append(callback)
        self.__client.loop_start()

    def __on_message(self, client, userdata, message: MQTTMessage):
        callbacks = self.__subscribers.get(message.topic, None)

        if callbacks is None:
            return

        for callback in callbacks:
            callback(message.payload.decode())
