stu = {'PECS001':{'phy':79,'chem':99,'mat':84,'bio':84},
       'PECS015':{'phy':79,'chem':99,'mat':84,'bio':84},
       'PECS065':{'phy':79,'chem':99,'mat':84,'bio':84},
       'PECS035':{'phy':79,'chem':99,'mat':84,'bio':84},
       'PECS038':{'phy':79,'chem':99,'mat':84,'bio':84}}
d={}
score_card={}
for key,marks in stu.items():
    d["Total"]=sum(marks.values())
    score_card["Percentage"]=d["Total"]/len(marks)
print("Total marks of each student ",d)
print("Percentage of each student ",score_card)
                            
