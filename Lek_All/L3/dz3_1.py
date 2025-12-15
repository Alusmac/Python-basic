a = float(input("Введіть перше число: "))
znak = input("Введіть дію яку треба зробити (+,-,*,/) : ")
b = float(input("Введіть друге число: "))

if znak == '+':
    res = a + b
elif znak == '-':
    res = a - b
elif znak == '*':
    res = a * b
elif znak == '/':
    if b == 0:
        print("Неможна поділити на нуль")
        res = None
    else:
        res = a / b
if res is not None:
    print("Буде:", res)



