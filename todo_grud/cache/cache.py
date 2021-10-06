from abc import abstractmethod
from typing import Protocol, Any


class CacheException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class Cache(Protocol):
    @abstractmethod
    def get(self, index: str):
        raise NotImplementedError

    @abstractmethod
    def add(self, key: str, value: Any):
        raise NotImplementedError

    @abstractmethod
    def remove(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def clear(self):
        raise NotImplementedError

    @abstractmethod
    def to_dic(self) -> dict:
        raise NotImplementedError
