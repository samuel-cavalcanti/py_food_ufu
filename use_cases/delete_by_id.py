from client_crud import Client
from cache import SingletonCache, CacheException


def delete_by_id(request):
    print("delete_by_id: ", request)
    client = Client(name=request.name, cpf=request.cpf, client_id=request.id,
                    favorite_food=request.favorite_food)

    cache = SingletonCache()

    c: Client = cache.get(client.id)

    if c is None:
        raise CacheException(f'cliente não encontrado {client.id}')

    cache.remove(client.id)

    return client
