import dataclasses
import hashlib

from task_grud import Task
from task_grud import SingletonTaskCache
from cache import CacheException
import json


def insert_task(task: Task) -> Task:
    cache = SingletonTaskCache()

    json_task = json.dumps(dataclasses.asdict(task))
    cache.add(task.title, json_task)

    return task
