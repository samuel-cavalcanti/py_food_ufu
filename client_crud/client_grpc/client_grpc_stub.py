import dataclasses

import grpc

from .generated_classes.crud_client_pb2_grpc import CrudClientServiceStub
from .generated_classes.crud_client_pb2 import Client


class ClientGrpcStub:

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50052')
        self.stub = CrudClientServiceStub(channel)

    def insert(self, client):
        return self.stub.insert(Client(**dataclasses.asdict(client)))

    def update(self, client):
        return self.stub.update(Client(**dataclasses.asdict(client)))
