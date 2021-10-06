import dataclasses

from todo_grud.cache.cache_repository import CacheRepository
from .task import Task

import json


def insert_task(task: Task) -> Task:
    print('insert_task', task)
    cache = CacheRepository.task_cache()
    print(f"task keys: {cache.to_dic().keys()}")
    print(f"id keys: {CacheRepository.client_id_cache().to_dic().keys()}")

    json_task = json.dumps(dataclasses.asdict(task))
    cache.add(f'{task.title}-{task.cid}', json_task)

    return task
