#a)
s= "mohandas Karamchand gandhi"
ss = ""
namelist = s.split()
for name in namelist[:len(namelist)-1]:
    ss=ss+name[0]+" "
ss=ss+namelist[-1]
print(ss)
#ss in uppercase
ss=ss.upper()
print(ss)
ss= ss.title()
print(ss)
s=s.title()
print(s)

print("")

#b)
s="bad python bad teacher bad lecture"
print("Replace all occurrences of bad to good =",s.replace("bad","good"))
print("Replace first occurrence of bad to good =",s.replace("bad","good",1))
s="bad python bad teacher bad lecture"
print("the leftmost bad is = ",s.index("bad"))
print("the second bad from left is = ",s.index("bad",s.index("bad")+len("bad")))
i=s.index("bad",s.index("bad")+len("bad"))
print(s[i:].replace("bad","worst",1))
print(s[:i]+s[i:].replace("bad","worst",1))
