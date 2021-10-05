import dataclasses
import json

from todo_grud.client_crud import Client
from todo_grud.mosquito_client import MosquittoClient, Topic
from todo_grud.client_crud.client_cache import SingletonClientCache


def insert_client(request_client: Client) -> Client:
    print("insert_client: ", request_client)

    '''
    Não deveria confiar que o request client está corretamente preenchido
    '''

    cache = SingletonClientCache()

    json_client = json.dumps(dataclasses.asdict(request_client))
    cache.add(request_client.id, json_client)

    try:
        mosquito_client = MosquittoClient()

        mosquito_client.publish_client(request_client, Topic.ADDED_CLIENTS)
    except ConnectionRefusedError:
        print("mosquitto não está ligado")
        pass

    return request_client
