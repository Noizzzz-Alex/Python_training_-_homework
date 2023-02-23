"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза.
Все числа натуральные и не превышают 30000.
"""
import  random
number_watermelon = int(input('введите общее количество арбузов: '))
max_index = 0
min_index = 30000
index = 1
while index <= number_watermelon:
    mass_watermelon = random.randint(1000, 30000)
    if mass_watermelon > max_index: max_index = mass_watermelon
    if mass_watermelon < min_index: min_index = mass_watermelon
    print(f'Масса арбуза № {index}  = {mass_watermelon} грамм\n')
    index += 1

print(f'арбуз для тещи - {min_index}, арбуз для себя - {max_index}')
