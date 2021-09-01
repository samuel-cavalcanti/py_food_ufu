import dataclasses

import grpc

from .generated_classes.crud_client_pb2_grpc import CrudClientServiceStub
from .generated_classes.crud_client_pb2 import GrpcClient


class ClientGrpcStub:

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50052')
        self.stub = CrudClientServiceStub(channel)

    def insert(self, client):
        return self.stub.insert(GrpcClient(**dataclasses.asdict(client)))

    def update(self, client):
        return self.stub.update(GrpcClient(**dataclasses.asdict(client)))

    def search_by_id(self, client):
        return self.stub.search_by_id(GrpcClient(**dataclasses.asdict(client)))

    def delete_by_id(self, client):
        return self.stub.delete_by_id(GrpcClient(**dataclasses.asdict(client)))
