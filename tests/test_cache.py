import unittest

from todo_grud.cache.singleton_cache import SingletonCache, CacheException


class TestSingletonCache(unittest.TestCase):

    @staticmethod
    def __test_add(index, value):
        cache = SingletonCache()
        cache.add(index, value)

    def test_cache(self):
        index = '0'
        value = 'test'
        self.__test_add(index, value)
        cache = SingletonCache()
        cache_value = cache.get(index)
        self.assertTrue(cache_value == value)

        with self.assertRaises(CacheException):
            cache.add(index, value)

        cache.remove(index)
        value = cache.get(index)
        self.assertTrue(value is None)

    def test_clear(self):
        cache = SingletonCache()
        key = '1313112312123'
        value = '2'
        cache.add(key, value)
        cache.add(key * 2, value)

        cache.clear()

        self.assertEqual(cache.get(key), None)
        self.assertEqual(cache.get(key * 2), None)


if __name__ == '__main__':
    unittest.main()
