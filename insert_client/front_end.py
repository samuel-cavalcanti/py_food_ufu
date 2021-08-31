import argparse
from argparse import ArgumentParser
import hashlib

from client import Client
from insert_client_grpc import InsertClientStub


def build_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(description='Adicionar clientes ADM CLI')
    parser.add_argument('--name', required=True, type=str, help='Nome do cliente')
    parser.add_argument('--cpf', required=True, type=str, help='CPF do cliente')

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    client_id = hashlib.sha256(f'{args.name}-{args.cpf} + um segredo :O'.encode()).hexdigest()

    client = Client(name=args.name, cpf=args.cpf, client_id=client_id, favorite_food="")

    stub = InsertClientStub()

    result = stub.insert(client)

    print(f"client: {client}")
    print(result)


if __name__ == '__main__':
    main()
