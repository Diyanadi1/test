#1

name = "Диана"
a = input("Введите Ваше имя: ")
if a in name:
    print("Привет,",a, "! О, это ж Я")
else: print("Привет, незнакомец!")


#2
import random

m = random.randint(1, 99) 
#print("Мое число:", m)

b = int(input("Введите Ваше число: "))
if b == m:
  print("Блин, угадал(")
else: 
    print("Не угадал, ХАХАХА!") 