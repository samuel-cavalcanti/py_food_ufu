from cache import SingletonCache, CacheException
from client_crud import Client
from mosquito_client import MosquittoClient


def insert_client(request) -> Client:
    print("insert_client: ", request)
    client = Client(name=request.name, cpf=request.cpf, client_id=request.id,
                    favorite_food=request.favorite_food)

    cache = SingletonCache()

    cache.add(client.id, client)

    mosquito_client = MosquittoClient()

    mosquito_client.publish_client(client)

    return client


def test_insert():
    client = Client(client_id='321312', favorite_food='arroz', cpf='123+1238+212', name='joao')

    insert_client(client)
    try:
        insert_client(client)
    except CacheException as e:
        print(e.args)


if __name__ == '__main__':
    test_insert()
