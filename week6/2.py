values=[("Rashma",8105731555,"rashma@gmail.com","Banglore"),("Bharathi",9276895311,"bharathi@yahoo.com","Coimbathore"),
        ("Deepthi",8976885553,"deepthi@gmail.com","Banglore"),("kakili",8816121598,"kakili@gmail.com","dispur")]
                                                             
Pho_book = dict(enumerate(values,1))
print("\n Phone book\n")
print(Pho_book)
print("adding a new entry to phone book")
Pho_book[len(Pho_book)+1]=[("sreenath",9872345670,"sreenath@pes.edu","kolar")]
print("after adding \n",Pho_book)
s=len(Pho_book)



#delete entry from phone book
key=int(input("enter key between to be deleted"))
if key in Pho_book:
    del Pho_book[key]
else:
    print("key not found")
print("after  deletion of key",key,"is \n",Pho_book)
