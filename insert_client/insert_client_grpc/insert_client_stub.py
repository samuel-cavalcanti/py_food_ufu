import grpc

from .generated_classes.insert_client_pb2_grpc import InsertClientServiceStub
from .generated_classes.insert_client_pb2 import InsertClientRequest


class InsertClientStub:

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50052')
        self.stub = InsertClientServiceStub(channel)

    def insert(self, client) -> str:
        client_request = InsertClientRequest(name=client.name, cpf=client.cpf, id=client.id)

        try:
            response = self.stub.insertNewClient(client_request)
            return response.result

        except grpc.RpcError as error:
            return error.__str__()
