from typing import Any, Optional
from todo_grud.cache.cache import Cache, CacheException


class SingletonCache(Cache):
    __slots__ = ['__table']
    __instance = None

    @staticmethod
    def instance():
        if SingletonCache.__instance is None:
            SingletonCache.__instance = SingletonCache()
        return SingletonCache.__instance

    def __init__(self):
        self.__table = dict()

    def get(self, index: str) -> Optional[Any]:
        return self.__table.get(index, None)

    def add(self, key: str, value: Any):
        if self.__table.get(key, None):
            raise CacheException('Já existe esse item')
        self.__table[key] = value

    def remove(self, key: str):
        del self.__table[key]

    def clear(self):
        self.__table = dict()

    def to_dic(self) -> dict:
        return self.__table
