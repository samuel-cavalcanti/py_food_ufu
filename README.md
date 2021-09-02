# Py Food:

[descrição do projeto](https://lasarojc.github.io/ds_notes/projeto/)

### todos

- Lembrar de como criar um env conda e por no readme
- Lembrar de colocar as portas das conexões em um ENV file
- Lembrar de colocar os nomes dos topicos na ENV file
- Lembrar de desacoplar o mosquitto client dos casos de uso, ou pensar mais sobre.
- Lembar de desacoplar a cache da regra de negócio tanto task quando client.

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

# executar testes de unidade

```shell
# executa testes de unidade nos client use cases
python -m unittest tests/test_client_use_cases.py -v  
# ecuta teste de unidade na implementação da cache
python -m unittest tests/test_cache.py -v
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