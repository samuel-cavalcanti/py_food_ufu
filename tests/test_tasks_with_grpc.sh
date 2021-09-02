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
python user_front_end.py d --cid 123;