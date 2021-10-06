import json

from todo_grud.cache.cache_repository import CacheRepository
from .task import Task


def search_task_by_cid(task: Task) -> list[Task]:
    print('search_task_by_cid', task)
    tasks = []

    cache = CacheRepository.task_cache()

    for json_task in cache.to_dic().values():
        current_task = Task(**json.loads(json_task))
        if task.cid == current_task.cid:
            tasks.append(current_task)

    return tasks
