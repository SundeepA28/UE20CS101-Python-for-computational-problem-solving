
#a)
f=open('mov1.csv')
l=f.read()
print(l)
f.close


#b)
f=open('mov1.csv','r')
f1=open('mov.txt','w')
l=f.readline()
while l:
    l=l.strip()
    s=l.split(',')
    print(s[0],s[-1],file=f1)
    l=f.readline()
f.close()
f1.close()
