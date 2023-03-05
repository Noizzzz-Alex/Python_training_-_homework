"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

*Пример:*

2 2
    4

"""
number_1 = 234
number_2 = 118

def recurs_summ(number_1, number_2, result=0):
    if number_1 == 0:
        if number_2 == 0:
            print(result)
            return
        else:
            result += 1
            recurs_summ(number_1, number_2 - 1, result)
    else:
        result += 1
        recurs_summ(number_1 - 1, number_2, result)


recurs_summ(number_1, number_2)
