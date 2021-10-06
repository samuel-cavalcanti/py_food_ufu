
#test search before insert
python admin_front_end.py s --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f;
#test insert
python admin_front_end.py i --cpf 123345 --name "Samuel Cavalcanti" --comida "pão de queijo";
#test search after insert
python admin_front_end.py s --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f;
#test update
python admin_front_end.py u --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f --comida "arroz";
#test search by id
python admin_front_end.py s --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f;
#test delete by id
python admin_front_end.py d --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f;
#test search after delete
python admin_front_end.py s --cid 37ccecd5c8b26b5b0f17fa7336b05f285804218ea0f7c066aa25f7eb499a906f;