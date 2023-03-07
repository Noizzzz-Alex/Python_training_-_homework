"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
initial_element = int(input('input 1st element: '))
step_count = int(input('input step: '))
quantity_elements = int(input('input quantity elements: '))

list_1 = [initial_element + step_count * _ for _ in range(quantity_elements)]
print(list_1)
