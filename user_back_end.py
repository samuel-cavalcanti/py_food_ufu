from concurrent import futures
from task_grud import TaskGrpcServer
from client_crud import Client
from task_use_cases import insert_task, update_task, delete_task, search_task_by_cid
from mosquito_client import MosquittoClient
import auth_use_case
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


def sub_clients(client, userdata, message):
    json_bytes_client: bytes = message.payload
    json_client = json_bytes_client.decode()
    c = Client(**json.loads(json_client))

    auth_use_case.listen_clients(c)

    pass


def main():
    task_grpc_server = TaskGrpcServer(insert_callback=insert,
                                      update_callback=update,
                                      search_callback=search,
                                      delete_callback=delete)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    task_grpc_server.add_to_grpc_server(server)

    port = '50053'

    print(f'user backend listening {port}')

    '''Porta está hard coded :O'''
    server.add_insecure_port('[::]:50053')
    server.start()
    MosquittoClient.subscribe_in_clients(sub_clients)
    server.wait_for_termination()


if __name__ == '__main__':
    main()