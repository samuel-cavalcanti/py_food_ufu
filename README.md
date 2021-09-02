# Py Food:

[descrição do projeto](https://lasarojc.github.io/ds_notes/projeto/)

### todos

- Lembrar de como criar um env conda e por no readme
- Lembrar de colocar as portas das conexões em um ENV file
- Lembrar de colocar os nomes dos topicos na ENV file
- Lembrar de colocar auth=True ou false na ENV file
- Lembrar de desacoplar o mosquitto client dos casos de uso, ou pensar mais sobre.
- Lembrar de desacoplar a cache da regra de negócio tanto task quando client.
- Lembrar de avaliar abstract factory para esse problema.
- Lembrar de esquecer, porque já tem muita coisa pra lembrar :sweat_smile:

```shell
#ativar o ambiente
conda activate py_food
```

## executar testes de integração client_CRUD

```shell
python admin_back_end.py
# outro terminal
mosquitto -v
# outro terminal
mosquitto_sub -t clients
# outro terminal

#teste insert
python admin_front_end.py i --cpf 123345 --name "Samuel Cavalcanti" --comida "pão de queijo"
#test update
python admin_front_end.py u --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f --comida "arroz"
#test search by id
python admin_front_end.py s --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f
#test delete by id
python admin_front_end.py d --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f
```
você também pode executar o script
```shell
# em um terminal
python admin_back_end.py
# outro terminal
mosquitto -v
# outro terminal
mosquitto_sub -t clients
# outro terminal
./tests/test_client_with_grpc.sh
```


## executar testes de integração task CRUD

Desabilite a autenticação

```python
#user_back_end.py
AUTH = False
```

```shell
#test insert
python user_front_end.py i --title "nova tarefa" --description "uma nova tarefa para fazer" --cid 123;
python user_front_end.py i --title "nova tarefa 2" --description "uma nova tarefa para fazer 2" --cid 123;
python user_front_end.py i --title "nova tarefa 3" --description "uma nova tarefa para fazer 3" --cid 123;
# test update task by cid
python user_front_end.py u --cid 123 --title "nova tarefa" --description "fiz um teste" ;
# test search by cid
python user_front_end.py s --cid 123;
# test delete with title
python user_front_end.py d --cid 123 --title "nova tarefa";
# test delete them all
python user_front_end.py d --cid 123
```

Você executar manualmente ou

```shell
# em outro terminal antes de executar o script
python user_back_end.py
# esteja na pasta raiz do repositório.
./tests/test_tasks_with_grpc.sh
```

# executar testes de unidade

```shell
# executa testes de unidade nos client use cases
python -m unittest tests/test_client_use_cases.py -v  
# ecuta teste de unidade na implementação da cache
python -m unittest tests/test_cache.py -v
# executar todos os testes de unidade
python -m unittest tests/test_all_components.py -v
```

### Informações para reprodução

veja que esse repositório possui a sua lista de pacotes python [requirements.txt](requirements.txt).
__É interessante usar uma virtual env__

```shell
#instalar todas as dependências
pip install -r requirements.txt
```

python version __3.9.6__

## configurações Grpc/proto

Comandos usados para compilar  _.proto_ files
[Grpc conf](Grpc_conf.md)