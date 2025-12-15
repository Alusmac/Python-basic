import string

a = input("Введіть 2 літери через дефіс: ")

start, end = a.split('-')
letters = string.ascii_letters

start_let = letters.index(start)
end_let = letters.index(end)

res = letters[start_let:end_let + 1]
print("Результат:", res)
