import unittest

from todo_grud.cache import CacheRepository,CacheException
from todo_grud.task_use_cases import Task
from todo_grud.client_use_cases import Client
from todo_grud.auth_use_case import AuthTasker, AuthException


class TestAuthUseCase(unittest.TestCase):
    def test_Task(self):
        task_a = Task(cid='0', title='title', description='cool description')
        client = Client(id='0', favorite_food='arroz', cpf='123+1238+212', name='joao')
        auth_tasker = AuthTasker(CacheRepository.client_id_cache())

        with self.assertRaises(AuthException):
            auth_tasker.auth_task(task_a)

        auth_tasker.add_id(client.id)

        with self.assertRaises(CacheException):
            auth_tasker.add_id(client.id)

        task_b = auth_tasker.auth_task(task_a)

        self.assertEqual(task_a, task_b)

        auth_tasker.remove_id(client.id)

        with self.assertRaises(AuthException):
            auth_tasker.auth_task(task_a)


if __name__ == '__main__':
    unittest.main()
