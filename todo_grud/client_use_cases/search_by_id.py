import json

from todo_grud.client_crud import Client
from todo_grud.cache import CacheException
from todo_grud.client_crud.client_cache import SingletonClientCache


def search_by_id(client: Client) -> Client:
    print("search_by_id: ", client)

    cache = SingletonClientCache()

    client = cache.get(client.id)

    if client is None:
        raise CacheException('Cache não possui esse cliente')  # Cache miss

    return Client(**json.loads(client))
