v=int(input("range till you need to generate cubes "))
cube = dict()
for x in range(1,v+1):
    cube[x]=pow(x,3)
print("The resultant dictionary with cube ass value numbers between 1 and ",v,"is\n",cube)
