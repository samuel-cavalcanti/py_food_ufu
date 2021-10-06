import json

from todo_grud.cache.cache_repository import CacheRepository
from .client import Client
from todo_grud.cache import CacheException


def delete_by_id(client: Client) -> Client:
    print("delete_by_id: ", client)

    cache = CacheRepository.client_cache()

    c: str = cache.get(client.id)

    if c is None:
        raise CacheException(f'cliente não encontrado {client.id}')

    removed_client = Client(**json.loads(c))
    cache.remove(client.id)

    return removed_client
