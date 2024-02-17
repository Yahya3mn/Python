#Write a Python program that calculates the area of a circle based on the radius entered by the user.
#Python: Area of a Circle
#In geometry, the area enclosed by a circle of radius r is πr2. Here the Greek letter π represents a constant, approximately equal to 3.14159,
#which is equal to the ratio of the circumference of any circle to its diameter.
from math import pi

r = float(input("Enter the radius of the circle : "))

area = pi*r**2

print("The area of the circle with radius" + str(r) + "is: " + str(area))