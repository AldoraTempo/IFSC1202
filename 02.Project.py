import math

def triangle_area():
  
a = float(input("Enter side 1 length: "))
print(a)
b = float(input("Enter side 2 length: "))
print(b)
c = float(input("Enter side 3 length: "))
print(c)

s = (a + b + c) / 2
print(s)

area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print("Area of the triangle is: area
triangle_area()
