from task_grud import Task
from .id_cache import SingletonIDCache


class AuthException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def auth_task(task: Task) -> Task:
    print(f'auth_task {task}')
    cache = SingletonIDCache()
    if cache.get(task.cid):
        return task

    raise AuthException('Usuário desconhecido')


def add_id(client_id: str):
    print(f'add_id:  {client_id}')

    cache = SingletonIDCache()
    if cache.get(client_id):
        return

    cache.add(client_id, client_id)


def remove_id(client_id: str):
    print(f'remove_client:  {client_id}')

    cache = SingletonIDCache()

    if cache.get(client_id):
        cache.remove(client_id)
