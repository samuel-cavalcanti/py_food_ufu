from client_crud import Client
from cache import SingletonCache, CacheException


def search_by_id(request):
    '''
        Talvez, a transformação do request em um estrutura como Client
        seja responsabilidade da camada inferior
    '''
    print("search_by_id: ", request)
    client = Client(name=request.name, cpf=request.cpf, client_id=request.id,
                    favorite_food=request.favorite_food)

    cache = SingletonCache()

    client = cache.get(client.id)

    if client is None:
        raise CacheException('Cache não possui esse cliente')

    return client
