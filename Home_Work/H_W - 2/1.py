"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть

"""
import random
coins = int(input('Введите количесво монет: '))
list_coins = []
eagle_counter = 0
tails_counter = 0
for i in range(coins):
    list_coins.append(random.randint(0,1))
    if list_coins[i] == 1:
        tails_counter += 1
    if list_coins[i] == 0:
        eagle_counter += 1
print(f'На столе лежат монеты 1- решка, 0- орел:  {list_coins}')
if tails_counter > eagle_counter:
    print(f'нужно перевернуть {eagle_counter} монет с орлом')
if tails_counter < eagle_counter:
    print(f'нужно перевернуть {tails_counter} монет с решкой')
if tails_counter == eagle_counter:
    print(f'т.к монет одинакого то только пользователю решать как ему удобнее')
