import unittest

from cache.singleton_cache import SingletonCache, CacheException


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


if __name__ == '__main__':
    unittest.main()
