# ~~Py Food~~ TODO GRUD:

[descrição do projeto](https://lasarojc.github.io/ds_notes/projeto/)

[![Build Status](https://app.travis-ci.com/samuel-cavalcanti/py_food_ufu.svg?branch=etapa_1)](https://app.travis-ci.com/samuel-cavalcanti/py_food_ufu)
[![codecov](https://codecov.io/gh/samuel-cavalcanti/py_food_ufu/branch/main/graph/badge.svg?token=CL5JBMV1A4)](https://codecov.io/gh/samuel-cavalcanti/py_food_ufu)

[Cobertura de testes da etapa 1](https://codecov.io/gh/samuel-cavalcanti/py_food_ufu/tree/etapa_1)

### todos

- Lembrar de colocar as portas das conexões em um ENV file
- Lembrar de colocar auth=True ou false na ENV file

```shell
#ativar o ambiente
conda activate py_food
```

## executar testes de integração com GRPC admin Front to Backend

```shell
# em um terminal
python admin_back_end.py
# outro terminal
./tests/grpc_test/test_client_with_grpc.sh
```

## executar testes de integração com GRPC User FrontEnd to BackEnd

Desabilite a autenticação

```python
# user_back_end.py
AUTH = False
```

```shell
# em outro terminal antes de executar o script
python user_back_end.py
# esteja na pasta raiz do repositório.
./tests/grpc_test/test_tasks_with_grpc.sh
```

## executar teste da Cache com Raft

```shell
cd tests/raft_test

python counter.py  3000 4000;

# outro terminal
python counter.py  4000 3000;

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