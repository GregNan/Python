﻿# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


# num = float(input('Введите число N:'))
# if (num>0):
#     b=num%10
#     c1=num//10
#     c=c1%10
#     d1=c1//10
#     d=d1%10
#     e1=d1//10
#     e=e1%10
#     a=b+c+d+e
# if (num<1):
#     num=num*10000
#     b=num%10
#     c1=num//10
#     c=c1%10
#     d1=c1//10
#     d=d1%10
#     e1=d1//10
#     e=e1%10
#     a=b+c+d+e
# print(a)
    


# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# a=1
# num = int(input('Введите число N:'))
# list =[]
# for i in range (1,num+1):
#     a*=i
#     list.append(a)
# print(list)
# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
# a=1
# b=0
# n = int(input('Введите число N:'))
# for i in range (n):
#     a=(1+1/n)**n
#     b+=a
#     print(b)

# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

# 18). Реализуйте алгоритм перемешивания списка.
# import random
# listA = ['a', 'b', 'c', 'd', 'e'] 
# random.shuffle(listA) 
# print(listA)
