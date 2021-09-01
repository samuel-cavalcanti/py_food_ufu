import json

from client_crud import Client
from cache import SingletonCache, CacheException


def delete_by_id(client: Client) -> Client:
    print("delete_by_id: ", client)

    cache = SingletonCache()

    c: str = cache.get(client.id)

    if c is None:
        raise CacheException(f'cliente não encontrado {client.id}')

    cache.remove(client.id)

    return Client(**json.loads(c))
