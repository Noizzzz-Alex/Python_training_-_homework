"""
Даны два массива чисел.
Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
Затем элементы второго массива
"""
import random

list_numbers_1 = [random.randint(1, 100) for i in range(int(input('Input size list #1: ')))]
list_numbers_2 = [random.randint(1, 100) for i in range(int(input('Input size list #2: ')))]

print(list_numbers_1)
print(list_numbers_2)