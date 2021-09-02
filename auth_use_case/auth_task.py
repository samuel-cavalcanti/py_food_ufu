from task_grud import Task
from client_crud import Client
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


def listen_clients(client: Client):
    print(f'listen_clients_list:  {client}')

    cache = SingletonIDCache()
    if cache.get(client.id):
        return

    cache.add(client.id, client.id)
