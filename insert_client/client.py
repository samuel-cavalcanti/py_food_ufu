from dataclasses import dataclass


@dataclass
class Client:
    '''Representação do meu cliente para que seja necessário criá-lo apatir do admin '''
    __slots__ = ['name', 'cpf', 'id']
    name: str
    cpf: str
    id: str

    def __init__(self, name: str, cpf, client_id: str):
        self.name = name
        self.cpf = cpf
        self.id = client_id

    def __str__(self):
        return f'name:{self.name} cpf:{self.cpf} id:{self.id}'
