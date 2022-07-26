#a)
s='''Respected Sir,\n I am here by enlisting all the programming languages we teach\n problem solving using python
 object oriented programming with C++\n java programming \nThanking You '''
pro_l=s.split(sep='\n')
for l in pro_l:
    print(l.title())
print("")
#b)
mac=['00','11','23','45','67','70']
print(':'.join(mac))
print("")
#c)
frnd=["","ram","sita","raj","joy","joe"]
print("  happy festival ".join(frnd))
print("")
#d)
srn="PE01 PE02 PE03 PE04 PE05 PE06 PE07 PE08 PE09 PE10"
print("Before replace :",srn)
rsrn = srn.replace("PE","PESU",3)
print("After replace : ",rsrn)
ser_srn = input("enter the srn to be search ")
found = rsrn.find(ser_srn.upper())
if(found>0):
    print(" is found at index ",found)
else:
    print(" srn not found")
        
