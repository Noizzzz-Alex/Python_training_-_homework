"""
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

numbers_sum = int(input('Введите сумму задаганных чисел: '))
numbers_multi = int(input('Введите произведение задаганных чисел: '))
c = False
for i in range(numbers_sum + numbers_multi):
    if c:
        break
    for j in range(numbers_sum + numbers_multi):
        if i + j == numbers_sum and i * j == numbers_multi:
            c = True
            print(f'Загаданные числа: {([i, j])}')
            break