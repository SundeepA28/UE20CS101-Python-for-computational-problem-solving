#Program with comments:
import random as r
heartrate=[]
for i in range(0,24,3):
	heartrate.append(r.randint(50,120))
print(heartrate)
countBrady = 0
countTachy = 0
for x in heartrate:
    if (x<=65):
        print("bradycardia")
        countBrady+=1
    elif (x>=100):
        print("tachycardia")
        countTachy+=1
    else:
     print("Normal")
print("")

# b) checking for any health risk
if countBrady>3 or countTachy >3:
    print("\nhealth risks detected")
else:
    print("Healthy Heart")
print("")
#c)
print("maximum heart rate=",max(heartrate),"bpm")    
print("minimum heart rate=",min(heartrate),"bpm")

