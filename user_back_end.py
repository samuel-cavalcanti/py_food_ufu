from concurrent import futures
from task_grud import TaskGrpcServer
from task_use_cases import insert_task, update_task, delete_task, search_task_by_cid
import grpc


def main():
    task_grpc_server = TaskGrpcServer(insert_callback=insert_task,
                                      update_callback=update_task,
                                      search_callback=search_task_by_cid,
                                      delete_callback=delete_task)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    task_grpc_server.add_to_grpc_server(server)

    port = '50053'

    print(f'user backend listening {port}')

    '''Porta está hard coded :O'''
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
