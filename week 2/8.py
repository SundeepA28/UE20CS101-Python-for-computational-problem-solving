k=float(input("enter the distance between two cities in kilometers is"))
m = k*1000             #converting into metre
c = m*100              #converting intocentimetre
f = c/30.48            #converting into feet
f= format(f,'.3f')
i = c/2.54             #converting into inches
i = format(i,'.3f')
print ("the distance in kilometers is ",k,"\nthe distance in meters is",
m,"\nthe distance in centimeters is ",c,"\nthe distance in feet is ",f,
"\nthe distance in inches is ",i)
