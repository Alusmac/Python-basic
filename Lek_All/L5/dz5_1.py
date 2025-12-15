#Користувач вводить рядок. чи може цей рядок бути ім'ям змінної?.
#Змінна не може:
#бути пустою
#починатися з цифри
#містити великі літери
#пробіл і знаки пунктуації(string.punctuation), окрім нижнього підкреслення _
#не може мати більше одного підкреслення _
#не може бути зарезервованим словом Python (keyword.kwlist)

import keyword
import string

text = input("Введіть свій варіант:")
result = True
if not text:
    result = False
elif text[0].isdigit():
    result = False
elif any(c.isupper() for c in text):
    result = False
elif any(c.isspace() or (c in string.punctuation and c != "_") for c in text):
    result = False
elif "__" in text:
    result = False
elif text in keyword.kwlist:
    result = False
print(result)
