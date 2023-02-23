"""
По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
"""
factorial = 5
n = 1
index = 1
while index <= factorial:
    n *= index
    index += 1
print(n)