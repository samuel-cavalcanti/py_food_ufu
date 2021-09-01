import argparse
from argparse import ArgumentParser
import hashlib

from client_crud import Client, ClientGrpcStub


def build_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(description='Adicionar clientes ADM CLI')
    parser.add_argument('action', type=str, choices=['i', 'u'],
                        help='diga a ação desejada "i"(insert) para Inserir novos dados e "u"(update) para atualizar um usuário ')
    parser.add_argument('--name', type=str, help='Nome do cliente')
    parser.add_argument('--cpf', type=str, help='CPF do cliente')
    parser.add_argument('--comida', type=str, help='comida favorida')
    parser.add_argument('--cid', type=str, help='CID(client id) indentificador único para cada cliente')

    return parser


def check_is_empty(arg):
    return arg if arg else ""


def insert_client(args):
    assert args.name, 'para inserir um cliente  --name não pode ser nulo'
    assert args.cpf, 'para inserir um cliente  cpf não pode ser nulo'

    favorite_food = check_is_empty(args.comida)

    client_id = hashlib.sha256(f'{args.name}-{args.cpf} + um segredo :O'.encode()).hexdigest()

    client = Client(name=args.name, cpf=args.cpf, client_id=client_id, favorite_food=favorite_food)

    stub = ClientGrpcStub()

    result = stub.insert(client)

    print(f"client: {client}")
    print(result)


def update_client(args):
    assert args.cid, 'para modificar um cliente  o cid não pode ser nulo'

    client = Client(name=check_is_empty(args.name),
                    cpf=check_is_empty(args.cpf),
                    client_id=args.cid,
                    favorite_food=check_is_empty(args.comida))

    stub = ClientGrpcStub()

    result = stub.update(client)

    print(f"client: {client}")
    print(result)


def main():
    parser = build_parser()
    args = parser.parse_args()
    actions = {'i': insert_client, 'u': update_client}
    actions[args.action](args)


if __name__ == '__main__':
    main()
