marks = [] 
x=1
while x>0:
    x = int(input("Enter marks or negative to stop : "))
    if x>0:
            marks.append(x)
print(marks)
# print maximum marks
max_marks = max(marks)
print("highest marks is:", max_marks)
count_max=marks.count(max_marks)
print("number of students who scored highest marks : ",count_max)
#print second highest marks
marks.sort(reverse=True)
print("marks entered are ",marks)
print("Second highest marks = ",marks[count_max])
fail_marks = int(input("enter fail marks : "))
if fail_marks in marks:
    c=marks.count(fail_marks)
    for  i in range(1,c+1):
        marks.remove(fail_marks)
else:
    print(fail_marks," is not present in the list")
print("new list is : ",marks)
