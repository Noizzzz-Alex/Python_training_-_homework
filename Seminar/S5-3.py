"""
напишите функцию, которая принимает одно число
и проверяет является ли оно простым.
"""


def prime_number(number):
    divider = 0
    i = 2
    while i < number - 1:
        result = number % i
        if result == 0:
            divider += 1
        i += 1
    if divider == 0:
        print('Число является простым')
    else:
        print('Число не простое')


def is_simple(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return print('Число не является простым')
        else:
            return print('Число простое')


prime_number(127)
is_simple(127)
