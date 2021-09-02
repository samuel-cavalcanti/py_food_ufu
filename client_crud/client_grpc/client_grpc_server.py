import dataclasses

import grpc
from concurrent import futures
from .generated_classes.crud_client_pb2_grpc import CrudClientService, add_CrudClientServiceServicer_to_server
from .generated_classes.crud_client_pb2 import GrpcClient

from ..client import Client


class ClientGrpcServer(CrudClientService):
    __slots__ = ['insert_client_callback', 'update_client_callback', 'search_client_callback', 'delete_client_callback']

    def __init__(self, insert_client_callback, update_client_callback, search_client_callback, delete_client_callback):
        self.insert_client_callback = insert_client_callback
        self.update_client_callback = update_client_callback
        self.search_client_callback = search_client_callback
        self.delete_client_callback = delete_client_callback

    @staticmethod
    def __request_to_client(request) -> Client:
        return Client(name=request.name, cpf=request.cpf, id=request.id,
                      favorite_food=request.favorite_food)

    def insert(self, request, context):
        client = self.__request_to_client(request)

        response = self.insert_client_callback(client)
        return GrpcClient(**dataclasses.asdict(response))

    def update(self, request, context):
        client = self.__request_to_client(request)

        response = self.update_client_callback(client)

        return GrpcClient(**dataclasses.asdict(response))

    def search_by_id(self, request, context):
        client = self.__request_to_client(request)

        response = self.search_client_callback(client)

        return GrpcClient(**dataclasses.asdict(response))

    def delete_by_id(self, request, context):
        client = self.__request_to_client(request)

        response = self.delete_client_callback(client)

        return GrpcClient(**dataclasses.asdict(response))

    def add_to_grpc_server(self, grpc_server):
        add_CrudClientServiceServicer_to_server(self, grpc_server)
