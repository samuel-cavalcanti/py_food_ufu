from client_crud import ClientGrpcServer
from client_use_cases import insert_client, update_client, search_by_id, delete_by_id


def main():
    server = ClientGrpcServer(insert_client_callback=insert_client,
                              update_client_callback=update_client,
                              search_client_callback=search_by_id,
                              delete_client_callback=delete_by_id)

    server.serve()


if __name__ == '__main__':
    main()
