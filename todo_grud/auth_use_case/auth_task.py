from todo_grud.task_use_cases import Task
from ..cache.cache import Cache


class AuthException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class AuthTasker:
    __cache: Cache

    def __init__(self, cache: Cache):
        self.__cache = cache

    def auth_task(self, task: Task) -> Task:
        print(f'auth_task {task}')

        print(f"in self.__cache: {self.__cache.get(task.cid)}")
        if self.__cache.get(task.cid):
            return task

        raise AuthException('Usuário desconhecido')

    def add_id(self, client_id: str):
        print(f'add_id:  {client_id}')

        if self.__cache.get(client_id):
            return

        self.__cache.add(client_id, client_id)

        print(f"added: {self.__cache.get(client_id)}")

    def remove_id(self, client_id: str):
        print(f'remove_client:  {client_id}')

        if self.__cache.get(client_id):
            self.__cache.remove(client_id)
