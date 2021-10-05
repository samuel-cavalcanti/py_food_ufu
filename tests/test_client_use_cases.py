import unittest

from cache.singleton_cache import CacheException
from client_crud import Client
from client_crud.client_cache import SingletonClientCache
from client_use_cases import insert_client, update_client, search_by_id, delete_by_id


class TestClientUseCases(unittest.TestCase):

    def setUp(self) -> None:
        SingletonClientCache().clear()

    def test_insert(self):
        client = Client(id='321312', favorite_food='arroz', cpf='123+1238+212', name='joao')
        client_2 = Client(id='321312', favorite_food='arroz', cpf='123+1238+212', name='joao')
        self.assertEqual(client, client_2)
        result = insert_client(client)

        self.assertEqual(client, result)

        with self.assertRaises(CacheException):
            insert_client(client)

    def test_update(self):
        fake_id = '111111'
        client = Client(id=fake_id, favorite_food='arroz', cpf='123+1238+212', name='joao')

        with self.assertRaises(CacheException):
            update_client(client)

        insert_client(client)

        new_client = client.copy_with(Client(id=fake_id, favorite_food='macarrão', cpf='', name='', ))

        result_client = update_client(new_client)

        self.assertEqual(result_client, new_client)

    def test_search_by_id(self):
        fake_id = '22222'
        client = Client(id=fake_id, favorite_food='arroz', cpf='123+1238+212', name='joao')
        insert_client(client)

        search_client = Client(id=fake_id, favorite_food='', cpf='', name='', )

        result = search_by_id(search_client)

        self.assertEqual(client, result)

        with self.assertRaises(CacheException):
            search_client = Client(id=':D', favorite_food='', cpf='', name='', )
            search_by_id(search_client)

    def test_delete(self):
        fake_id = '33333'
        client = Client(id=fake_id, favorite_food='arroz', cpf='123+1238+212', name='joao')

        with self.assertRaises(CacheException):
            search_client = Client(id=fake_id, favorite_food='', cpf='', name='', )
            delete_by_id(search_client)

        insert_client(client)
        search_client = Client(id=fake_id, favorite_food='', cpf='', name='', )
        result = delete_by_id(search_client)

        self.assertEqual(result, client)

        with self.assertRaises(CacheException):
            search_by_id(search_client)


if __name__ == '__main__':
    unittest.main()
