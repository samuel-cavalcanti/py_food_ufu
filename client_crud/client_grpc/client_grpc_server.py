import dataclasses

import grpc
from concurrent import futures
from .generated_classes.crud_client_pb2_grpc import CrudClientService, add_CrudClientServiceServicer_to_server
from .generated_classes.crud_client_pb2 import Client


class ClientGrpcServer(CrudClientService):
    __slots__ = ['insert_client_callback', 'update_client_callback', 'search_client_callback', 'delete_client_callback']

    def __init__(self, insert_client_callback, update_client_callback, search_client_callback, delete_client_callback):
        self.insert_client_callback = insert_client_callback
        self.update_client_callback = update_client_callback
        self.search_client_callback = search_client_callback
        self.delete_client_callback = delete_client_callback

    def insert(self, request, context):
        response = self.insert_client_callback(request)
        return Client(**dataclasses.asdict(response))

    def update(self, request, context):
        response = self.update_client_callback(request)

        return Client(**dataclasses.asdict(response))

    def search_by_id(self, request, context):
        response = self.search_client_callback(request)

        return Client(**dataclasses.asdict(response))

    def delete_by_id(self, request, context):
        response = self.delete_client_callback(request)

        return Client(**dataclasses.asdict(response))

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_CrudClientServiceServicer_to_server(self, server)
        port = '50052'

        print(f'listening {port}')

        '''Porta está hard coded :O'''
        server.add_insecure_port('[::]:50052')
        server.start()
        server.wait_for_termination()
