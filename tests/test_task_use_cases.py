import unittest

from todo_grud.task_use_cases import Task
from todo_grud.task_use_cases import insert_task, update_task, search_task_by_cid, delete_task
from todo_grud.cache import CacheException, CacheRepository


class TestTaskUseCases(unittest.TestCase):

    def setUp(self):
        cache = CacheRepository.task_cache()
        cache.clear()

    def test_insert(self):
        task_a = Task(cid='0', title='title', description='cool description')
        task_b = Task(cid='0', title='title', description='cool description')
        task_c = Task(cid='1', title='title', description='cool description')
        self.assertEqual(task_a, task_b)
        self.assertNotEqual(task_a, task_c)

        result = insert_task(task_a)
        self.assertEqual(task_a, result)

        '''Inserindo tarefa com mesmo titulo e descrição mas diferentes cids'''
        result = insert_task(task_c)
        self.assertEqual(result, task_c)

        with self.assertRaises(CacheException):
            insert_task(task_b)

    def test_update(self):
        title = 'title'
        better_description = 'better then cool description'
        task_a = Task(cid='2', title=title, description='cool description')
        insert_task(task_a)
        new_task = task_a.copy_with(Task(cid='', title='', description=better_description))
        result = update_task(new_task)

        task_c = Task(cid='2', title=title, description=better_description)

        self.assertEqual(result, task_c)

        with self.assertRaises(CacheException):
            update_task(Task(cid='', title='', description='better then cool description'))

    def test_search_by_cid(self):
        fake_cid = '123213213214122332134124321211'

        query_task = Task(cid=fake_cid, title='', description='')

        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(cid='2', title='title', description='cool description'))

        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(cid=fake_cid, title='title2', description='cool description'))
        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 1)

        insert_task(Task(cid=fake_cid, title='title3', description='cool description'))
        insert_task(Task(cid=fake_cid, title='title4', description='cool description'))
        insert_task(Task(cid=fake_cid, title='title5', description='cool description'))

        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 4)

    def test_delete_task(self):
        fake_cid = '34567892131245345243123'
        fake_title = 'custom title'
        query_task = Task(cid=fake_cid, title='', description='')

        result = delete_task(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(cid=fake_cid, title='title1', description='cool description'))
        insert_task(Task(cid=fake_cid, title='title2', description='cool description'))
        insert_task(Task(cid=fake_cid, title='title3', description='cool description'))

        result = delete_task(query_task)

        self.assertEqual(len(result), 3)

        result = delete_task(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(cid=fake_cid, title='title', description='cool description'))
        insert_task(Task(cid=fake_cid, title=fake_title, description='cool description'))
        insert_task(Task(cid=fake_cid, title='title2', description='cool description'))

        query_task = Task(cid=fake_cid, title=fake_title, description='')
        result = delete_task(query_task)

        self.assertEqual(len(result), 1)

        result = delete_task(query_task)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
