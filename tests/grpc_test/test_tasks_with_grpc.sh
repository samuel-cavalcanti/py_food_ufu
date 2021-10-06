#insert client
python admin_front_end.py i --cpf 123345 --name "Samuel Cavalcanti" --comida "pão de queijo";

CID=37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f

# search before insert
python user_front_end.py s --cid $CID;
#test insert
python user_front_end.py i --title "nova tarefa" --description "uma nova tarefa para fazer" --cid $CID;
python user_front_end.py i --title "nova tarefa 2" --description "uma nova tarefa para fazer 2" --cid $CID;
python user_front_end.py i --title "nova tarefa 3" --description "uma nova tarefa para fazer 3" --cid $CID;
# search after insert
python user_front_end.py s --cid $CID;
# test update task by cid
python user_front_end.py u --cid $CID --title "nova tarefa" --description "fiz um teste" ;
# test search by cid
python user_front_end.py s --cid $CID;
# test delete with title
python user_front_end.py d --cid $CID --title "nova tarefa";
# test search by cid after delete
python user_front_end.py s --cid $CID;
# test delete them all
python user_front_end.py d --cid $CID;

#test delete client
python admin_front_end.py d --cid $CID;