while True:
    a = float(input("Введіть перше число: "))
    znak = input("Введіть дію яку треба зробити (+,-,*,/) : ")
    b = float(input("Введіть друге число: "))

    res = None
    if znak == '+':
        res = a + b
    elif znak == '-':
        res = a - b
    elif znak == '*':
        res = a * b
    elif znak == '/':
        if b == 0:
            print("Неможна поділити на нуль")
        else:
            res = a / b
    else:
        print("Невірна операція")

    if res is not None:
        print("Буде:", res)

    zapit = input("Бажаєте ще рахувати? (yes - так): ").lower()
    if zapit not in ('yes'):
        print("Гарної днини")
        break
