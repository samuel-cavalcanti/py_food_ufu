from argparse import ArgumentParser
from todo_grud.grpc import TaskGrpcStub
from todo_grud.task_use_cases import Task


def build_parser(actions: list[str]) -> ArgumentParser:
    help_message = '''digite a ação desejada\n
      "i"(insert) para Inserir nova tafera \n
      "u"(update) para atualizar uma tarefa\n
      "s"(search) para buscar taferas, podendo filtrar por titulo e descrição\n
      "d"(delete) para deletar todas as  taferas pelo cid ou filtradas por titulo ou descrição"'''
    parser = ArgumentParser(description='Adicionar taferas User CLI')
    parser.add_argument('action', type=str, choices=actions,
                        help=help_message)
    parser.add_argument('--description', type=str, help='descrição da tarefa', default="")
    parser.add_argument('--title', type=str, help='titulo da tafera', default="")
    parser.add_argument('--cid', type=str, help='CID(client id) indentificador único para cada cliente', default="")

    return parser


def insert_task(task: Task):
    assert task.cid, 'é obrigatório ter cid para inserir a tarefa'
    assert task.title, 'é obrigatório uma tarefa ter um titlo para inserir a tarefa'
    assert task.description, 'é obrigatório uma tarefa ter uma descrição para inserir a tarefa'

    stub = TaskGrpcStub()

    result = stub.insert(task)

    print(f'insert task: {task}')
    print(f'result: {result}')
    pass


def update_task(task: Task):
    assert task.cid, 'é obrigatório ter cid para atualizar a tarefa'
    assert task.title, 'é obrigatório ter um titulo para atualizar a tarefa'
    print(f'update_task task: {task}')
    stub = TaskGrpcStub()

    result = stub.update(task)

    print(result)


def search_by_cid(task: Task):
    assert task.cid, 'é obrigatório ter cid para buscar as tarefas'
    print(f'search_by_cid task: {task}')

    stub = TaskGrpcStub()
    result = stub.search_by_cid(task)

    print(result)

    pass


def delete_task(task: Task):
    assert task.cid, 'é obrigatório ter cid para deltar as tarefas'
    print(f'delete_task task: {task}')
    stub = TaskGrpcStub()
    result = stub.delete_by_cid(task)

    print(result)
    pass


def main():
    actions = {'i': insert_task, 'u': update_task, 's': search_by_cid, 'd': delete_task}
    parser = build_parser(list(actions.keys()))
    args = parser.parse_args()
    task = Task(cid=args.cid, title=args.title, description=args.description)
    actions[args.action](task)


if __name__ == '__main__':
    main()
