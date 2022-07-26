n = int(input("enter the number of students "))
k = int(input("enter the number of apples "))
t = k//n #finds the number of apples each students gets
l=k%n   #finds the number of apples remaining in the basket
print("each student will get",t,"apples")
print("number of apples left in the basket",l)
