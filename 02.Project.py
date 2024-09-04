import math

a = float(input("Enter side 1: "))
print(a)
b = float(input("Enter side 2: "))
print(b)
c = float(input("Enter side 3: "))
print(c)
s = (a + b + c) / 2
area = math.sqrt(s * (s * a) * (s * b) * (s * c))
print(area)
if a + b > c and a + c > b and b + c > a:
        print("The area of the triangle is: area")
else:
        print("The lengths do not form a triangle")