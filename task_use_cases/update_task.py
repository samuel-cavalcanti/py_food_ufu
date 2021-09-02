import dataclasses

from task_grud import Task

from task_grud import Task
from task_grud import SingletonTaskCache
from cache import CacheException
import json


def update_task(task: Task) -> Task:
    cache = SingletonTaskCache()

    old_task_json = cache.get(task.id)

    if old_task_json is None:
        raise CacheException('task não existe na cache')

    old_task = Task(**json.loads(old_task_json))

    new_task = old_task.copy_with(task)

    new_task_json = json.dumps(dataclasses.asdict(new_task))

    cache.remove(old_task.id)
    cache.add(new_task.id, new_task_json)

    return new_task
