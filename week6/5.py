f1=open('mov1.csv','r')
d=dict()
for i in f1:
    i=i.strip()
    s=i.split(',')
    if s[0] not in d:
        d[s[0]]=[]
        d[s[0]].insert(0,s[2])
        i=f1.readline()
print(d)
