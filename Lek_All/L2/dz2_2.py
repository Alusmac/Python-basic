#variant 4
num = int(input("Введіть будь ласка ціле число:"))

a = num // 10000
b = (num // 1000) % 10
c = (num // 100) % 10
d = (num // 10) % 10
e = num % 10

answer = e * 10000 + d * 1000 + c * 100 + b * 10 + a

print("Результат:", answer)

# variant 5  #Сподіваюсь що хоть це підійде
import math

n = int(input("Введіть число:" ))
digits = int(math.log10(n)) + 1

rev = 0
rev += (n % 10) * int(math.pow(10, digits - 1))
rev += (n // 10 % 10) * int(math.pow(10, digits - 2))
rev += (n // 100 % 10) * int(math.pow(10, digits - 3))
rev += (n // 1000 % 10) * int(math.pow(10, digits - 4))
rev += (n // 10000 % 10) * int(math.pow(10, digits - 5))

print("Результат:", rev)

#Варінт 1
#s = int(input("Введіть будь ласка ціле число :"))
#a = s // 10000
#b = s % 10000 // 1000
#c = s % 1000 // 100
#d = s % 100 // 10
#e = s % 10
#print(e, d, c, b, a, sep="")

##Варіант 2
#n = int(input("Введіть будь ласка ціле число :"))
#print(n % 10,n % 100 // 10,n % 1000 // 100,n % 10000 // 1000,n // 10000,sep="")

#Варіант 3.
#a = int(input("Введіть будь ласка ціле число:"))
#b = 0
#while a > 0:
#    digit = a % 10
#    a = a // 10
#   b = b * 10
#    b = b + digit
#print("Bаріант 3-й","Зворотнє число :" , b)










