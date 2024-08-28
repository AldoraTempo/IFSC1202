import math

a = int (input("Enter number of students:"))
print(a)
b = int (input("Enter number of students:"))
print(b)
c = int (input("Enter number of students:"))
print(c)


deska = math.floor(a / 2)
deskb = math.floor(b / 2)
deskc = math.floor(c / 2)
dtf = deska + deskb + deskc
print(dtf)
ea = a % 2
eb = b % 2
ec = c % 2
edt = ea + eb + ec
td = dtf + edt
print(td)