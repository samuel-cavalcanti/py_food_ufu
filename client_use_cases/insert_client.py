from cache import SingletonCache, CacheException
from client_crud import Client
from mosquito_client import MosquittoClient


def insert_client(request_client: Client) -> Client:
    print("insert_client: ", request_client)

    '''
    Não deveria confiar que o request client está corretamente preenchido
    '''

    cache = SingletonCache()

    cache.add(request_client.id, request_client)

    ''' MosquiTTo retorna um Exception se não conseguir conectar devo trata-lo'''

    mosquito_client = MosquittoClient()

    mosquito_client.publish_client(request_client)

    return request_client


def test_insert():
    client = Client(client_id='321312', favorite_food='arroz', cpf='123+1238+212', name='joao')

    insert_client(client)
    try:
        insert_client(client)
    except CacheException as e:
        print(e.args)


if __name__ == '__main__':
    test_insert()