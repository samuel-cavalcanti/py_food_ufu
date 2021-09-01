'''
Copiei do stackoverflow o que é que pode dar errado
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
'''


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CacheException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class SingletonCache(metaclass=Singleton):
    __slots__ = ['__table']

    def __init__(self):
        self.__table = dict()

    def get(self, index: str):
        return self.__table.get(index, None)

    def add(self, key: str, value):
        if self.__table.get(key, None):
            raise CacheException('Já existe esse item')
        self.__table[key] = value

    def remove(self, key: str):
        del self.__table[key]

    def to_dic(self) -> dict:
        return self.__table
