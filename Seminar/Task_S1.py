"""
В некоторой школе решили набрать три новых математических класса
и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.
**Input:**
20
21
22
**Output:**
32
"""

class_1 = int(21)
class_2 = int(21)
class_3 = int(20)
desk_1 = (class_1 + 1)//2
desk_2 = (class_2 + 1)//2
desk_3 = (class_3 + 1)//2

school_desk = desk_1+desk_2+desk_3
print(f'необходимое количество парт : {school_desk}')


