import random
import math


# Задача 10.
# number_сoins = int(input('Введите количество монет на столе '))
# choice_coins_list = [random.randint(0,1) for i in range(0, number_сoins)]
#         # орел - 1
#         # решка - 0
# print(choice_coins_list)
# eagle = choice_coins_list.count(1)
# tails = choice_coins_list.count(0)
# if eagle == tails:
#     print('Не имеет значение, количество монет перевернутых орлом равно монетам с решкой')
# elif eagle == number_сoins:
#     print('Все монеты перевернуты орлом')
# elif tails == number_сoins:
#     print('Все монеты перевернуты решкой')
# elif eagle > tails:
#     print(f'Проще перевернуть монеты с решкой, их {tails} шт.')
# else:
#     print(f'Проще перевернуть монеты с орлом, их {eagle} шт.')

# Задача 12.
# def numbers(amount, product):
#     for x in range(1, 1001):
#         y = amount - x
#         if x * y == product:
#             return x, y
#     return None
#
#
# summa = int(input("Введите сумму чисел: "))
# proizvedenie = int(input("Введите произведение чисел: "))
# result = numbers(summa, proizvedenie)
# if result:
#     print(f"X = {result[0]} Y = {result[1]}")
# else:
#     print("Невозможно определить числа X и Y по заданным значениям S и P.")

# Задача 14.
# num = int(input('Введите число '))
# stepen = 0
# result = 1
# while result < num:
#     print(result)
#     stepen = stepen + 1
#     result = 2 ** stepen

# Задача 1*
# num = int(input('Введите число '))
# result = 0
# while num > 9:
#     units = num % 10
#     num = num // 10
#     result = result + units
# result = result + num
# print(result)

# Задача 3*
# num = int(input("Введите число "))
# list_division = []
# for i in range(1, num+1):
#     if num % i == 0:
#         list_division.append(i)
# print(list_division)
