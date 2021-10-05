import dataclasses

from todo_grud.task_grud import Task
from todo_grud.task_grud import SingletonTaskCache
from todo_grud.cache import CacheException
import json


def update_task(task: Task) -> Task:
    print('update_task', task)
    cache = SingletonTaskCache()

    old_task_json = cache.get(f'{task.title}-{task.cid}')

    if old_task_json is None:
        raise CacheException('task não existe na cache')

    old_task = Task(**json.loads(old_task_json))

    new_task = old_task.copy_with(task)

    new_task_json = json.dumps(dataclasses.asdict(new_task))

    cache.remove(f'{old_task.title}-{old_task.cid}')
    cache.add(f'{new_task.title}-{new_task.cid}', new_task_json)

    return new_task
