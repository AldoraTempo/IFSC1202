o1 = float(input("Enter the first operand: "))
print(o1)
op = input("Enter an operator (+, -, *, /): ")
print(op)
o2 = float(input("Enter the second operand: "))
print(o2)

if op == '+':
  res = o1 + o2
  print(f"{o1} + {o2} = {res}")
elif op == '-':
  res = o1 - o2
  print(f"{o1} - {o2} = {res}")
elif op == '*':
  res = o1 * o2
  print(f"{o1} * {o2} = {res}")
elif op == '/':
  if o2 != 0:
    res = o1 / o2
    print(f"{o1} / {o2} = {res}")
  else:
      print("Error")
else:
    print("Invalid Operator")
