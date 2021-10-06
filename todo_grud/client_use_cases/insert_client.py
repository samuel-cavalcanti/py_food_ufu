import dataclasses
import json

from todo_grud.cache.cache_repository import CacheRepository
from .client import Client



def insert_client(request_client: Client) -> Client:
    print("insert_client: ", request_client)

    '''
    Não deveria confiar que o request client está corretamente preenchido
    '''

    cache = CacheRepository.client_cache()

    json_client = json.dumps(dataclasses.asdict(request_client))
    cache.add(request_client.id, json_client)

    return request_client
