from .cache import Cache
from todo_grud.cache.singletons.task_cache import SingletonTaskCache
from todo_grud.cache.singletons.client_cache import SingletonClientCache
from todo_grud.cache.raft_protocol.sync_client_cache import SyncClientIDCache


class CacheRepository:

    @staticmethod
    def client_cache() -> Cache:
        return SingletonClientCache.instance()

    @staticmethod
    def task_cache() -> Cache:
        return SingletonTaskCache.instance()

    @staticmethod
    def client_id_cache() -> Cache:
        return SingletonClientCache.instance()

    @staticmethod
    def user_backend_sync_cache() -> Cache:
        return SyncClientIDCache('localhost:50070', ['localhost:50060', 'localhost:50080'])  # 'localhost:50055'

    @staticmethod
    def admin_backend_sync_cache() -> Cache:
        return SyncClientIDCache('localhost:50060', ['localhost:50070', 'localhost:50080'])  # 'localhost:50054'
