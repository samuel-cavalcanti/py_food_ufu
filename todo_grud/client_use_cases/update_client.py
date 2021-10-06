import dataclasses
import json

from todo_grud.cache.cache_repository import CacheRepository
from .client import Client
from todo_grud.cache import CacheException


def update_client(client: Client) -> Client:
    print("update_client: ", client)

    cache = CacheRepository.client_cache()

    old_client_json: str = cache.get(client.id)

    if old_client_json is None:
        raise CacheException('Não é possível atualizar a cache pois não tem nada')

    old_client = Client(**json.loads(old_client_json))

    cache.remove(client.id)

    new_client = old_client.copy_with(client)

    new_client_json = json.dumps(dataclasses.asdict(new_client))
    cache.add(client.id, new_client_json)

    return new_client
