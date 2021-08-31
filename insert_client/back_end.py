from client import Client
from insert_client_grpc import InsertClientServer
from mosquito_server import MosquittoClient

''' um brinde as boas práticas!'''
table = dict()


def insert_client(request) -> str:
    client = Client(name=request.name, cpf=request.cpf, client_id=request.id,
                    favorite_food=request.favorite_food)

    if table.get(client.id, None):
        raise Exception('Cliente já existe!!!')

    table[client.id] = client

    mosquito_client = MosquittoClient()

    mosquito_client.publish_client(client)

    return "Criado com sucesso!!"


def main():
    server = InsertClientServer(insert_client)
    server.serve()


if __name__ == '__main__':
    main()
