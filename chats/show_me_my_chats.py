import json
with open('chats.json','r', encoding='utf8') as f:
    chats = eval(f.read())

for x in chats:
    print(f"{x} : {chats[x]}\n")