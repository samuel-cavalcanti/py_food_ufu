from dataclasses import dataclass


@dataclass
class Client:
    '''Representação do meu cliente para que seja necessário criá-lo apatir do admin '''
    __slots__ = ['name', 'cpf', 'id', 'favorite_food']
    name: str
    cpf: str
    id: str
    favorite_food: str

    def __init__(self, name: str, cpf, id: str, favorite_food: str):
        self.name = name
        self.cpf = cpf
        self.id = id
        self.favorite_food = favorite_food

    def __str__(self):
        return f'name:{self.name} cpf:{self.cpf} id:{self.id} food:{self.favorite_food}'

    def __eq__(self, other):
        assert isinstance(other, Client)

        return self.id == other.id and self.cpf == other.cpf and self.name == other.name and self.favorite_food == other.favorite_food

    def copy_with(self, client):
        name = client.name if client.name else self.name
        cpf = client.cpf if client.cpf else self.cpf
        cid = client.id if client.id else self.id
        food = client.favorite_food if client.favorite_food else self.favorite_food

        return Client(name=name, cpf=cpf, id=cid, favorite_food=food)
