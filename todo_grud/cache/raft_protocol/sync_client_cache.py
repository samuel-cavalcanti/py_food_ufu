from pysyncobj import SyncObj
from typing import List, Any

from pysyncobj.batteries import ReplDict
from todo_grud.cache.cache import Cache, CacheException


class SyncClientIDCache(Cache):
    __dict_of_ids: ReplDict
    __sync: SyncObj

    def __init__(self, current_node: str, another_nodes: List[str]):
        self.__dict_of_ids = ReplDict()
        self.__sync = SyncObj(current_node, another_nodes, consumers=[self.__dict_of_ids])

    def get_leader(self):
        return self.__sync._getLeader()

    def get(self, index: str):
        return self.__dict_of_ids.get(index)

    def add(self, key: str, value: Any):
        if self.get(key):
            raise CacheException(f"{key} exist !!")
        self.__dict_of_ids.set(key, value, sync=True)

    def remove(self, key: str):
        self.__dict_of_ids.set(key, None, sync=True)

    def clear(self):
        self.__dict_of_ids.clear()

    def to_dic(self) -> dict:
        return self.__dict_of_ids.rawData()
