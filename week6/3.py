Stu_marks=['PECS001','PECS015''PECS065''PECS035''PECS038']
p1 =[98,99,85,92,79]
c1 = [91,90,84,98,99]
m1 = [78,39,60,50,84]
b1 =[95,59,78,80,89]
mks1={}
s = 0
for i in Stu_marks :
    mks1[i]={"Physics":p1[s],"Chemistry":c1[s],"Mathematics":
    m1[s],"Biology":b1[s]}
    s+=1
print("Marks sheet dictionary :",mks1)    
