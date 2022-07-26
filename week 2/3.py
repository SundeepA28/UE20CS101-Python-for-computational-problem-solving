x1 = float(input("enter the x coordinate of the first point "))
y1 = float(input("enter the y coordinate of the first point "))
x2 = float(input("enter the x coordinate of the second point "))
y2 = float(input("enter the y coordinate of the second point "))
import math
distance = math.sqrt(((x2-x1)**2 + (y2-y1)**2)) # using formula to find the distance
print("the distance between two points is = ",distance)
