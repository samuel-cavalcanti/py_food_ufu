import unittest

from task_grud import Task
from task_use_cases import insert_task, update_task, search_task_by_cid, delete_task
from cache import CacheException


class TestTaskUseCases(unittest.TestCase):
    def test_insert(self):
        task_a = Task(id='0', cid='0', title='title', description='cool description')
        task_b = Task(id='0', cid='0', title='title', description='cool description')
        task_c = Task(id='0', cid='1', title='title', description='cool description')
        self.assertEqual(task_a, task_b)
        self.assertNotEqual(task_a, task_c)

        result = insert_task(task_a)
        self.assertEqual(task_a, result)

        with self.assertRaises(CacheException):
            insert_task(task_b)

    def test_update(self):
        fake_id = '1'
        task_a = Task(id=fake_id, cid='2', title='title', description='cool description')
        insert_task(task_a)
        new_task = Task(id=fake_id, cid='', title='', description='better then cool description')
        result = update_task(new_task)

        task_c = Task(id=fake_id, cid='2', title='title', description='better then cool description')

        self.assertEqual(result, task_c)

        with self.assertRaises(CacheException):
            update_task(Task(id='42', cid='', title='', description='better then cool description'))

    def test_search_by_cid(self):
        fake_cid = '123213213214122332134124321211'

        query_task = Task(id='', cid=fake_cid, title='', description='')

        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(id='32132131242131231', cid='2', title='title', description='cool description'))

        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(id='34567890', cid=fake_cid, title='title', description='cool description'))
        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 1)

        insert_task(Task(id='852456', cid=fake_cid, title='title', description='cool description'))
        insert_task(Task(id='5892349598893934', cid=fake_cid, title='title', description='cool description'))
        insert_task(Task(id='009439509643012840', cid=fake_cid, title='title', description='cool description'))

        result = search_task_by_cid(query_task)
        self.assertEqual(len(result), 4)

    def test_delete_task(self):
        fake_cid = '34567892131245345243123'
        fake_title = 'custom title'
        query_task = Task(id='', cid=fake_cid, title='', description='')

        result = delete_task(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(id='32132131231234', cid=fake_cid, title='title', description='cool description'))
        insert_task(Task(id='123312312', cid=fake_cid, title='title', description='cool description'))
        insert_task(Task(id='123432432423', cid=fake_cid, title='title', description='cool description'))

        result = delete_task(query_task)

        self.assertEqual(len(result), 3)

        result = delete_task(query_task)
        self.assertEqual(len(result), 0)

        insert_task(Task(id='32132131231234', cid=fake_cid, title='title', description='cool description'))
        insert_task(Task(id='123312312', cid=fake_cid, title=fake_title, description='cool description'))
        insert_task(Task(id='123432432423', cid=fake_cid, title='title', description='cool description'))

        query_task = Task(id='', cid=fake_cid, title=fake_title, description='')
        result = delete_task(query_task)

        self.assertEqual(len(result), 1)

        result = delete_task(query_task)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
