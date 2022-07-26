#Program with Comments:
# A)

# initialize list 
l1 = ["facebook",{23,89},{8.4,9.3},"twitter",25,90,"whatsapp",55,44,
      ("p","e","s"),45,0.9,9.5,2,150,(78,56),[45,90,23],["pesacademy","pesu"]]
l_int = [];l_float=[];l_str=[];l_tuple=[];l_list=[];l_set=[]
for i in l1:
    c=type(i)
    if(c==int):
        l_int.append(i)
    elif(c==float):
        l_float.append(i)
    elif(c==str):
        l_str.append(i)
    elif(c==list):
        l_list.append(i)
    else:
        l_set.append(i)
# printing result 
print("Integer list : ",l_int) 
print("String list : ",l_str)
print("float list : ",l_float)
print("list type : ",l_list)
print("tuple list : ",l_tuple)
print("")

#B)
srt=['hi','yeah','ok','good']
numb=[1,89,56,78,34,9,64]
print(" before sorting the string list: ",srt)
print(" before sorting the number list: ",numb)
srt.sort()    # compute sorting of list of string and number
numb.sort()
print(" after sorting the string list(ascending): ",srt)
print(" after sorting the number list(ascending): ",numb)

#slicing for decreasing order
print(" after sorting the string list(decending): ",srt[::-1]) 
print(" after sorting the number list(decending): ",numb[::-1])

