from client_crud import Client
from cache import SingletonCache, CacheException
from mosquito_client import MosquittoClient


def update_client(request):
    print("update_client: ", request)
    client = Client(name=request.name, cpf=request.cpf, client_id=request.id,
                    favorite_food=request.favorite_food)

    cache = SingletonCache()

    old_client: Client = cache.get(client.id)

    if old_client is None:
        raise CacheException('Não é possível atualizar a cache pois não tem nada')

    cache.remove(client.id)

    new_client = old_client.copy_with(client)
    cache.add(client.id, new_client)

    '''
    Talvez Subject-Observer resolva esse problema de duplicação
    '''
    mosquito_client = MosquittoClient()

    mosquito_client.publish_client(new_client)

    return new_client
