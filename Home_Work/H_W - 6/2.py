"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

user_range_min = int(input('  Введите нижний предел диапазона: '))
user_range_max = int(input(' Введите верхний предел диапазона: '))
list_1 = [random.randint(-50, 50) for _ in range(50)]
list_2 = [i for i in range(len(list_1)) if user_range_min <= list_1[i] <= user_range_max]
print(list_1)
print(list_2)
