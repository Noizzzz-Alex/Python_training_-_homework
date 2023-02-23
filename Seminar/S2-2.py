"""
Дано натуральное число A > 1.
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.
"""
number = int(input('input number: '))
count = 3
fibonaci_n=2
fibonaci_min_1 = 1
#fibonaci_min_2 = 1
while fibonaci_n<number:
    temp = fibonaci_n
    fibonaci_n = fibonaci_n + fibonaci_min_1
    fibonaci_min_1 = temp
    count += 1

if number == fibonaci_n:
    print(f'Number - {number} = {count}')
else:
    print('no')




