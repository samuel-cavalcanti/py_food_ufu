from client_crud import Client
from cache import SingletonCache, CacheException


def search_by_id(client: Client) -> Client:
    print("search_by_id: ", client)

    cache = SingletonCache()

    client = cache.get(client.id)

    if client is None:
        raise CacheException('Cache não possui esse cliente')

    return client
