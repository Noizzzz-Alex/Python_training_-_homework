"""
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
input_number = int(input('Введите трехзнчное число : '))
digit_1 = input_number//100
digit_2 = input_number%100//10
digit_3 = input_number%10


print(f'Sum digit = {digit_1 + digit_2 + digit_3}')