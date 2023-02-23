"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

number = int(input('Введите число: '))
count_2k = 1
degree = 0
while count_2k < number:
    count_2k *= 2
    if count_2k < number:
        degree += 1
        print(f'2 в степени {degree} = {count_2k}')
