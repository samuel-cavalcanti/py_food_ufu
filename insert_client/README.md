## Atualizar o grpc

```shell
cd insert_client_grpc
python -m grpc_tools.protoc -I./protos --python_out=./generated_classes --grpc_python_out=./generated_classes protos/insert_client.proto
```
talvez tenha que colocar o _from_ pontinho _._  nas classes geradas _não lembro se concertei isso :)_
```python
from . import ...#
```


## executar o back e o front

```shell
conda activate py_food
python back_end.py
# outro terminal
python fron_end.py
```
