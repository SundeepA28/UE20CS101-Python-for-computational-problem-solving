num = int(input("enter the four digit number "))
th = num//1000  #finding the digits that are entered 
num = num%1000
h = num//100
num = num%100
t = num//10
num = num%10
u = num
print ("the number of the digit are =",th,h,t,u)
sum = u+t+h+th #finding the sum of all digits
print("the sum of the digits is ",sum)
