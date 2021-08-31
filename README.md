# Py Food: 

### todos 
 - Lembrar de como criar um env conda e por no readme
 - Lembrar de colocar as portas das conexões em um ENV file
 - Lembrar de colocar os nomes dos topicos na ENV file 

```
#ativar o ambiente
conda activate py_food
```

```
# atualizar o grpc
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. protos/helloworld.proto
```