import grpc
from concurrent import futures
from .generated_classes.insert_client_pb2_grpc import InsertClientServiceServicer, \
    add_InsertClientServiceServicer_to_server
from .generated_classes.insert_client_pb2 import InsertNewClientResponse


class InsertClientServer(InsertClientServiceServicer):

    def __init__(self, callback_function):
        self.callback = callback_function

    def insertNewClient(self, request, context):
        """Retorna o resultado da criação do """
        content = {'name': request.name, 'cpf': request.cpf, 'client_id': request.id}
        return InsertNewClientResponse(result=self.callback(content))

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_InsertClientServiceServicer_to_server(self, server)

        '''Porta está hard coded :O'''
        server.add_insecure_port('[::]:50052')
        server.start()
        server.wait_for_termination()
