## Atualizar o grpc

### Client

```shell
# vá para a pasta client_grpc
cd client_grpc
python -m grpc_tools.protoc -I./protos --python_out=./generated_classes --grpc_python_out=./generated_classes protos/crud_client.proto
```

Lembrar de colocar o _from_ pontinho _._  nas classes geradas

```python
# crud_client_pb2_grpc.py
from . import crud_client_pb2 as crud__client__pb2
```

### Task

```python
from . import crud_task_pb2 as crud__task__pb2
```

```shell
# vá para a pasta task_grpc
cd task_grpc
python -m grpc_tools.protoc -I./protos --python_out=./generated_classes --grpc_python_out=./generated_classes protos/crud_task.proto
```
