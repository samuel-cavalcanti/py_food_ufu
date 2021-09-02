import dataclasses

import grpc

from .generated_classes.crud_task_pb2_grpc import CrudTaskServiceStub
from .generated_classes.crud_task_pb2 import GrpcTask


class TaskGrpcStub:

    def __init__(self):
        channel = grpc.insecure_channel('localhost:50052')
        self.__stub = CrudTaskServiceStub(channel)

    def insert(self, task):
        return self.__stub.insert(GrpcTask(**dataclasses.asdict(task)))

    def update(self, task):
        return self.__stub.update(GrpcTask(**dataclasses.asdict(task)))

    def search_by_cid(self, task):
        return self.__stub.search_by_cid(GrpcTask(**dataclasses.asdict(task)))

    def delete_by_id(self, task):
        return self.__stub.delete_by_id(GrpcTask(**dataclasses.asdict(task)))