from dataclasses import dataclass


@dataclass
class Task:
    cid: str
    title: str
    description: str
    __slots__ = ['cid', 'title', 'description']

    def __init__(self, cid: str, title: str, description: str):
        self.cid = cid
        self.title = title
        self.description = description

    def __str__(self):
        return f'id:{self.id} cid:{self.cid} title:{self.title} description:{self.description}'

    def copy_with(self, task):
        assert isinstance(task, Task)
        cid = task.cid if task.cid else self.cid
        title = task.title if task.title else self.title
        description = task.description if task.description else self.description

        return Task(cid=cid, title=title, description=description)
