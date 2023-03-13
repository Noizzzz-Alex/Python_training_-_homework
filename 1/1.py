"""
Задание на строки
Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов,
иначе дополнить строку символами 'o' до длины 12.
"""
import random
import string

added_letter = 'o'
len_string = random.randint(1, 20)
string_user = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_string))
print(f'string: {string_user}  | len_string: {len_string}')
if len(string_user) > 10:
    print(string_user[:6])
else:
    while len_string < 12:
        string_user += added_letter
        len_string += 1
    print(f'finish_string: {string_user} | len_string:{len_string}')
