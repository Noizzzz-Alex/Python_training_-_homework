"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

"""

len_set_1 = int(input('Введите размер первого множества: '))
len_set_2 = int(input('Введите размер второго множества: '))
i = 0
set_user_1 = set()
set_user_2 = set()
while i < len_set_1:
    temp_input = int(input('Введите число 1-го множества: '))
    set_user_1.add(temp_input)
    i += 1
i = 0
while i < len_set_2:
    temp_input = int(input('Введите число 2-го множества: '))
    set_user_2.add(temp_input)
    i += 1

union_sets = set_user_1.union(set_user_2)
list_temp = list(union_sets)
list_temp.sort()

print(list_temp)
