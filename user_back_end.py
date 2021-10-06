from concurrent import futures

from todo_grud.cache import CacheRepository
from todo_grud.grpc import TaskGrpcServer
from todo_grud.client_use_cases import Client
from todo_grud.task_use_cases import insert_task, update_task, delete_task, search_task_by_cid
from todo_grud.auth_use_case import AuthTasker
import grpc
import json

AUTH = True


auth_tasker = AuthTasker(CacheRepository.user_backend_sync_cache())


def insert(task):
    if AUTH:
        return insert_task(auth_tasker.auth_task(task))
    else:
        return insert_task(task)


def update(task):
    if AUTH:
        return update_task(auth_tasker.auth_task(task))
    else:
        return update_task(task)


def search(task):
    if AUTH:
        return search_task_by_cid(auth_tasker.auth_task(task))
    else:
        search_task_by_cid(task)


def delete(task):
    return delete_task(auth_tasker.auth_task(task))


def added_client(json_client):
    client = Client(**json.loads(json_client))
    auth_tasker.add_id(client.id)


def removed_client(json_client):
    client = Client(**json.loads(json_client))
    auth_tasker.remove_id(client.id)


def main():
    task_grpc_server = TaskGrpcServer(insert_callback=insert,
                                      update_callback=update,
                                      search_callback=search,
                                      delete_callback=delete)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    task_grpc_server.add_to_grpc_server(server)

    port = '50053'

    print(f'user backend listening {port}')
    server.add_insecure_port(f'[::]:{port}')
    server.start()

    server.wait_for_termination()


if __name__ == '__main__':
    main()
