td = int(input("Enter total days: "))
y = td // 365
r = td % 365
w = r // 7
d = r % 7
print(y)
print(w)
print(d)