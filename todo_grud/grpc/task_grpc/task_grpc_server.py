import dataclasses

from .generated_classes.crud_task_pb2 import GrpcTask, GrpcTaskList
from .generated_classes.crud_task_pb2_grpc import CrudTaskService, add_CrudTaskServiceServicer_to_server

from todo_grud.task_use_cases.task import Task


class TaskGrpcServer(CrudTaskService):
    __slots__ = ['__insert_callback', '__update_callback', '__search_callback', '__delete_callback']

    def __init__(self, insert_callback, update_callback, search_callback, delete_callback):
        self.__insert_callback = insert_callback
        self.__update_callback = update_callback
        self.__search_callback = search_callback
        self.__delete_callback = delete_callback

    @staticmethod
    def __grpc_task_to_task(grpc_task) -> Task:
        return Task(cid=grpc_task.cid, title=grpc_task.title, description=grpc_task.description)

    @staticmethod
    def __task_list_to_grpc_task_list(tasks: list[Task]) -> GrpcTaskList:
        grpc_task_list = GrpcTaskList()
        grpc_task_list.tasks.extend([GrpcTask(**dataclasses.asdict(t)) for t in tasks])
        return grpc_task_list

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
        return self.__task_list_to_grpc_task_list(tasks)

    def delete_by_cid(self, request, context):
        task = self.__grpc_task_to_task(request)
        tasks = self.__delete_callback(task)
        return self.__task_list_to_grpc_task_list(tasks)

    def add_to_grpc_server(self, grpc_server):
        add_CrudTaskServiceServicer_to_server(self, grpc_server)
