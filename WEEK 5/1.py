l=["panipuri","dosa","bhelpuri","masala dosa","dahipuri","ravadosa","pizza topings","pizza mania"]
chat=[]
dosa=[]
pizza=[]
for s in l:
    if(s.endswith("puri")):
       chat.append(s)
    if (s.endswith("dosa")):
        dosa.append(s)
    if(s.startswith("pizza")):
        pizza.append(s)
print("chats = ",chat,"\ndosa = ",dosa,"\npizza = ",pizza)
