import unittest
from task_grud import Task
from client_crud import Client
from auth_use_case import auth_task, add_id, remove_id, AuthException


class TestAuthUseCase(unittest.TestCase):
    def test_Task(self):
        task_a = Task(cid='0', title='title', description='cool description')
        client = Client(id='0', favorite_food='arroz', cpf='123+1238+212', name='joao')

        with self.assertRaises(AuthException):
            auth_task(task_a)

        add_id(client.id)

        task_b = auth_task(task_a) 

        self.assertEqual(task_a, task_b)

        remove_id(client.id)

        with self.assertRaises(AuthException):
            auth_task(task_a)


if __name__ == '__main__':
    unittest.main()
