from concurrent import futures

import grpc

from todo_grud.grpc import ClientGrpcServer
from todo_grud.client_use_cases import insert_client, update_client, search_by_id, delete_by_id, Client
from todo_grud.cache.cache_repository import CacheRepository

sync_client_id = CacheRepository.admin_backend_sync_cache()


def insert(client: Client) -> Client:
    client = insert_client(client)
    sync_client_id.add(client.id, client.id)
    return client


def delete(client: Client) -> Client:
    client = delete_by_id(client)
    sync_client_id.remove(client.id)
    return client


def main():
    client_grpc_server = ClientGrpcServer(insert_client_callback=insert,
                                          update_client_callback=update_client,
                                          search_client_callback=search_by_id,
                                          delete_client_callback=delete)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    client_grpc_server.add_to_grpc_server(server)

    port = '50052'

    print(f'admin backend listening {port}')

    '''Porta está hard coded :O'''
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
