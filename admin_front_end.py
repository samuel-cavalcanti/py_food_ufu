import argparse
from argparse import ArgumentParser
import hashlib

from client_crud import Client, ClientGrpcStub


def build_parser(actions: list[str]) -> ArgumentParser:
    parser = argparse.ArgumentParser(description='Adicionar clientes ADM CLI')
    parser.add_argument('action', type=str, choices=actions,
                        help='diga a ação desejada "i"(insert) para Inserir novos dados e "u"(update) para atualizar um usuário ')
    parser.add_argument('--name', type=str, help='Nome do cliente', default="")
    parser.add_argument('--cpf', type=str, help='CPF do cliente', default="")
    parser.add_argument('--comida', type=str, help='comida favorida', default="")
    parser.add_argument('--cid', type=str, help='CID(client id) indentificador único para cada cliente', default="")

    return parser


def insert_client(client: Client):
    assert client.name, 'para inserir um cliente  --name não pode ser nulo'
    assert client.cpf, 'para inserir um cliente  cpf não pode ser nulo'

    client_id = hashlib.sha256(f'{client.name}-{client.cpf} + um segredo :O'.encode()).hexdigest()

    new_client = Client(name=client.name, cpf=client.cpf, id=client_id, favorite_food=client.favorite_food)

    stub = ClientGrpcStub()

    result = stub.insert(new_client)

    print(f"client: {client}")
    print(result)


def update_client(client: Client):
    assert client.id, 'para modificar um cliente  o cid não pode ser nulo'

    stub = ClientGrpcStub()

    result = stub.update(client)

    print(f"client: {client}")
    print(result)


def search_by_cid(client: Client):
    assert client.id, 'para buscar informações de um cliente  o cid não pode ser nulo'

    stub = ClientGrpcStub()

    result = stub.search_by_id(client)

    print(f"client: {client}")
    print(result)


def delete_by_cid(client: Client):
    assert client.id, 'para deletar  um cliente  o cid não pode ser nulo'

    stub = ClientGrpcStub()

    result = stub.delete_by_id(client)

    print(f"client: {client}")
    print(result)
    pass


def main():
    actions = {'i': insert_client, 'u': update_client, 's': search_by_cid, 'd': delete_by_cid}
    parser = build_parser(list(actions.keys()))
    args = parser.parse_args()
    client = Client(name=args.name, cpf=args.cpf,
                    id=args.cid, favorite_food=args.comida)

    actions[args.action](client)


if __name__ == '__main__':
    main()
