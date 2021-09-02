from task_grud import Task, SingletonTaskCache

from .search_task_by_cid import search_task_by_cid


def delete_task(task: Task) -> list[Task]:
    deleted_task = []
    tasks = search_task_by_cid(task)
    cache = SingletonTaskCache()
    for current_task in tasks:
        if current_task.copy_with(task) == current_task:
            deleted_task.append(current_task)
            cache.remove(current_task.id)

    return deleted_task
