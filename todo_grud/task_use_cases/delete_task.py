from .search_task_by_cid import search_task_by_cid
from ..cache.cache_repository import CacheRepository
from .task import Task


def delete_task(task: Task) -> list[Task]:
    print('delete_task', task)
    deleted_task = []
    tasks = search_task_by_cid(task)
    cache = CacheRepository.task_cache()
    for current_task in tasks:
        if current_task.copy_with(task) == current_task:
            deleted_task.append(current_task)
            cache.remove(f'{current_task.title}-{current_task.cid}')

    return deleted_task
