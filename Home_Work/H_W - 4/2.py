"""

Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.

"""
import random

bed_size = random.randint(10, 20)
garden_bed = list()
for i in range(bed_size):
    garden_bed.append(random.randint(1, 100))
i = int(input(f'Общее количество кустов: {bed_size}, укажите номер интересующего куста: '))
temp_sum = garden_bed[i - 1] + garden_bed[i] + garden_bed[i + 1]

print(garden_bed)
print(f'общее количество возможного сбора ягод: {temp_sum} грамм')
