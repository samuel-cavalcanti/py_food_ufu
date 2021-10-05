from concurrent import futures
from todo_grud.task_grud import TaskGrpcServer
from todo_grud.client_crud import Client
from todo_grud.task_use_cases import insert_task, update_task, delete_task, search_task_by_cid
from todo_grud.mosquito_client import MosquittoClient, Topic
from todo_grud import auth_use_case
import grpc
import json

AUTH = True

'''Talvez seja a hora de avaliar um abstract factory CRUD ? '''


def insert(task):
    if AUTH:
        return insert_task(auth_use_case.auth_task(task))
    else:
        return insert_task(task)


def update(task):
    if AUTH:
        return update_task(auth_use_case.auth_task(task))
    else:
        return update_task(task)


def search(task):
    if AUTH:
        return search_task_by_cid(auth_use_case.auth_task(task))
    else:
        search_task_by_cid(task)


def delete(task):
    return delete_task(auth_use_case.auth_task(task))


'''Não sei pra que serve client e userdata, espero não importante'''


def added_client(json_client):
    client = Client(**json.loads(json_client))
    auth_use_case.add_id(client.id)


def removed_client(json_client):
    client = Client(**json.loads(json_client))
    auth_use_case.remove_id(client.id)


def main():
    task_grpc_server = TaskGrpcServer(insert_callback=insert,
                                      update_callback=update,
                                      search_callback=search,
                                      delete_callback=delete)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    task_grpc_server.add_to_grpc_server(server)

    mosquito = MosquittoClient()

    mosquito.subscribe_in_topic(callback=added_client, topic=Topic.ADDED_CLIENTS)
    mosquito.subscribe_in_topic(callback=removed_client, topic=Topic.REMOVED_CLIENTS)

    port = '50053'

    print(f'user backend listening {port}')

    '''Porta está hard coded :O'''
    server.add_insecure_port('[::]:50053')
    server.start()

    server.wait_for_termination()


if __name__ == '__main__':
    main()
