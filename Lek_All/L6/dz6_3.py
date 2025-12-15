a = int(input("Введіть число: "))

while a > 9:
    x = 1
    for digit in str(a):
        x *= int(digit)
    a = x
print(a)
