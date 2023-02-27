"""
Первая задача:
Задаем длину списка наполненного рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
"""
import random

search_number = int(input('Введите искомое число: '))
list_numbers = [random.randint(1, 100) for i in range(20)]
print(list_numbers)
count_search = 0
for i in range(len(list_numbers)):
    if list_numbers[i] == search_number:
        count_search += 1

if count_search > 0:
    print(f'Число: {search_number} встречается в заданном списке {count_search} раз.')
else:

    print(f'Такого числа нет')
    min_nearest_number = search_number - 1
    temp_min = search_number - 1
    # Поиск минимального ближайшего числа к искомому
    # list_min = []
    for i in range(len(list_numbers)):
        if list_numbers[i] < search_number:
            if (search_number - list_numbers[i]) < temp_min:
                temp_min = (search_number - list_numbers[i])
                min_nearest_number = list_numbers[i]

    # Поиск максимального ближайшего числа
    max_nearest_number = search_number + 1
    temp_max = search_number + 1
    for i in range(len(list_numbers)):
        if list_numbers[i] > search_number:
            if (list_numbers[i] - search_number) < temp_max:
                temp_max = (list_numbers[i] - search_number)
                max_nearest_number = list_numbers[i]

    if (max_nearest_number - search_number) < (search_number - min_nearest_number):
        print(f'ближайшее число большe искомого: {max_nearest_number}')
    if (max_nearest_number - search_number) > (search_number - min_nearest_number):
        print(f'ближайшее число меньшe искомого: {min_nearest_number}')
    if (max_nearest_number - search_number) == (search_number - min_nearest_number):
        print(f'оба числа равны! меньшее ближайшее : {min_nearest_number} и большее ближайшее: {max_nearest_number}')


















