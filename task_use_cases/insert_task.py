import dataclasses
from task_grud import Task
from task_grud import SingletonTaskCache
import json


def insert_task(task: Task) -> Task:
    print('insert_task', task)
    cache = SingletonTaskCache()

    json_task = json.dumps(dataclasses.asdict(task))
    cache.add(f'{task.title}-{task.cid}', json_task)

    return task
