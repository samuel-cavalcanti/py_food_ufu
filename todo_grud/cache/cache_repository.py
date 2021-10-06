from .cache import Cache
from .singletons.task_cache import SingletonTaskCache
from .singletons.client_cache import SingletonClientCache
from .raft_protocol.sync_client_cache import SyncClientIDCache
from .singletons.id_cache import SingletonIDCache
from .singletons.singleton_cache import SingletonCache


class CacheRepository:
    __client_cache: Cache = None
    __task_cache: Cache = None
    __client_id_cache: Cache = None

    @staticmethod
    def client_cache() -> Cache:
        if CacheRepository.__client_cache is None:
            CacheRepository.__client_cache = SingletonCache()
        return CacheRepository.__client_cache

    @staticmethod
    def task_cache() -> Cache:
        if CacheRepository.__task_cache is None:
            CacheRepository.__task_cache = SingletonCache()

        return CacheRepository.__task_cache

    @staticmethod
    def client_id_cache() -> Cache:
        if CacheRepository.__client_id_cache is None:
            CacheRepository.__client_id_cache = SingletonCache()
        return CacheRepository.__client_id_cache

    @staticmethod
    def user_backend_sync_cache() -> Cache:
        if CacheRepository.__client_id_cache is None:
            CacheRepository.__client_id_cache = SyncClientIDCache('localhost:7000',
                                                                  ['localhost:8000'])
        return CacheRepository.__client_id_cache

    @staticmethod
    def admin_backend_sync_cache() -> Cache:
        if CacheRepository.__client_id_cache is None:
            CacheRepository.__client_id_cache = SyncClientIDCache('localhost:8000', ['localhost:7000'])
        return CacheRepository.__client_id_cache
