# a)   interchanging values using temporary variable
a = float(input("enter the value of a "))
b = float(input("enter the value of b "))
print("the value of a before interchanging is ",a)
print("the value of b before interchanging is ",b)
temp = a
a=b
b=temp
print ("the value of a after interchanging is ",a)
print("the value of b after interchanging is ",b)
print()

#  b)  interchanging values without using temporary variable
a = float(input("enter the values of a "))
b = float(input("enter the values of b "))
print("the value of a before interchanging is ",a)
print("the value of b before interchanging is ",b)
a = a+b
b = a-b
a = a-b
print("the value of a after interchanging is ",a)
print("the value of b after interchanging is ",b)

