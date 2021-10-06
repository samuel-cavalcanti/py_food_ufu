import json

from todo_grud.cache.cache_repository import CacheRepository
from .client import Client
from todo_grud.cache import CacheException


def search_by_id(client: Client) -> Client:
    print("search_by_id: ", client)

    cache = CacheRepository.client_cache()

    client = cache.get(client.id)

    if client is None:
        raise CacheException('Cache não possui esse cliente')  # Cache miss

    return Client(**json.loads(client))
