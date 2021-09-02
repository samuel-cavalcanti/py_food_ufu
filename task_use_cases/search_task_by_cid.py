import json

from task_grud import Task
from task_grud import SingletonTaskCache


def search_task_by_cid(task: Task) -> list[Task]:
    tasks = []

    cache = SingletonTaskCache()

    for json_task in cache.to_dic().values():
        current_task = Task(**json.loads(json_task))
        if task.cid == current_task.cid:
            tasks.append(current_task)

    return tasks
