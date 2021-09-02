import dataclasses

from .generated_classes.crud_task_pb2 import GrpcTask, GrpcTaskList
from .generated_classes.crud_task_pb2_grpc import CrudTaskService, add_CrudTaskServiceServicer_to_server

from ..task import Task


class TaskGrpcServer(CrudTaskService):
    __slots__ = ['__insert_callback', '__update_callback', '__search_callback', '__delete_callback']

    def __init__(self, insert_callback, update_callback, search_callback, delete_callback):
        self.__insert_callback = insert_callback
        self.__update_callback = update_callback
        self.__search_callback = search_callback
        self.__delete_callback = delete_callback

    @staticmethod
    def __grpc_task_to_task(grpc_task) -> Task:
        return Task(id=grpc_task.id, cid=grpc_task.cid, title=grpc_task.title, description=grpc_task.description)

    def insert(self, request, context):
        task = self.__grpc_task_to_task(request)
        response = self.__insert_callback(task)
        return GrpcTask(**dataclasses.asdict(response))

    def update(self, request, context):
        task = self.__grpc_task_to_task(request)
        response = self.__update_callback(task)
        return GrpcTask(**dataclasses.asdict(response))

    def search_by_cid(self, request, context):
        task = self.__grpc_task_to_task(request)
        tasks = self.__search_callback(task)
        return GrpcTaskList([GrpcTask(**dataclasses.asdict(t)) for t in tasks])

    def delete_by_id(self, request, context):
        task = self.__grpc_task_to_task(request)
        tasks = self.__delete_callback(task)
        return GrpcTaskList([GrpcTask(**dataclasses.asdict(t)) for t in tasks])