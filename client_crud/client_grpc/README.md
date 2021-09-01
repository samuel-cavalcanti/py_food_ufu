## Atualizar o grpc

```shell
cd client_grpc
python -m grpc_tools.protoc -I./protos --python_out=./generated_classes --grpc_python_out=./generated_classes protos/crud_client.proto
```
Lembrar de colocar o _from_ pontinho _._  nas classes geradas 
```python
#crud_client_pb2_grpc.py
from . import crud_client_pb2 as crud__client__pb2
```