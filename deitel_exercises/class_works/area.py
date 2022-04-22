import math
# Press the variable dot tab tab will show you all the methods you can perform on itd

radius_str = input("Enter the radius of the circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print("The circumference is: ", circumference, " and the area is: ", area)
