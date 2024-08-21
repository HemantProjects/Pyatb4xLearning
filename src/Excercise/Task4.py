# Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2```
import math

radius = float(input("Please enter radius of the circle:- "))

area1 = math.pi * (radius ** 2)
area2 = 3.14 * (radius ** 2)
print("Area of circle is = ", area1)
print("Area of circle is = ", area2)
