from concurrent import futures

import grpc

from client_crud import ClientGrpcServer
from client_use_cases import insert_client, update_client, search_by_id, delete_by_id
from task_grud import TaskGrpcServer
from task_use_cases import insert_task, update_task, delete_task, search_task_by_cid


def main():
    client_grpc_server = ClientGrpcServer(insert_client_callback=insert_client,
                                          update_client_callback=update_client,
                                          search_client_callback=search_by_id,
                                          delete_client_callback=delete_by_id)

    task_grpc_server = TaskGrpcServer(insert_callback=insert_task,
                                      update_callback=update_task,
                                      search_callback=search_task_by_cid,
                                      delete_callback=delete_task)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    client_grpc_server.add_to_grpc_server(server)
    task_grpc_server.add_to_grpc_server(server)
    port = '50052'

    print(f'listening {port}')

    '''Porta está hard coded :O'''
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
