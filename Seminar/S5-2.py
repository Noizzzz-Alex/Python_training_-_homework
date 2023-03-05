"""
Хакер Василий получил доступ к классному журналу и хочет заменить
все свои минимальные оценки на максимальные. напишите программу, которая заменяет все оценки Василия
но наоборот все максимальные на минимальные.
"""
import random

size_grade_book = random.randint(15, 25)
grade_book = list(random.randint(1, 5) for _ in range(size_grade_book))
print(f'Изначальные оценки: {grade_book}')
for i in range(len(grade_book)):
    if grade_book[i] == 5:
        grade_book[i] = 1
    if grade_book[i] == 4:
        grade_book[i] = 2

        # print(grade_book[i])

print(f'Измененные оценки: {grade_book}')
