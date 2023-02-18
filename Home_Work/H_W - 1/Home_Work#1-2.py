"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
 Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""
ticket = int(input('Введите номер билета(6 цифр) : '))
digit_1 = ticket//100000
digit_2 = ticket//10000%10
digit_3 = ticket//1000%10
digit_4 = ticket//100%10
digit_5 = ticket//10%10
digit_6 = ticket%10
if (digit_1 + digit_2 +digit_3) == (digit_4 + digit_5 + digit_6):
    print('yes')
else:
    print('no')
