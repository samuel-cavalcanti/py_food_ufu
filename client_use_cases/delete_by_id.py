import json

from client_crud import Client
from cache import CacheException
from client_crud import SingletonClientCache
from mosquito_client import MosquittoClient, Topic


def delete_by_id(client: Client) -> Client:
    print("delete_by_id: ", client)

    cache = SingletonClientCache()

    c: str = cache.get(client.id)

    if c is None:
        raise CacheException(f'cliente não encontrado {client.id}')

    removed_client = Client(**json.loads(c))
    cache.remove(client.id)

    ''' MosquiTTo retorna um Exception se não conseguir conectar devo trata-lo'''

    try:
        mosquito_client = MosquittoClient()

        mosquito_client.publish_client(removed_client, Topic.REMOVED_CLIENTS)
    except ConnectionRefusedError:
        print("mosquitto não está ligado")
        pass

    return removed_client
