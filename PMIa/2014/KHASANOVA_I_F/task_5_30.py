# Задача 5. Вариант 30.
# Напишите программу, которая бы при запуске случайным образом отображала
# имя одного из трех племянников Скруджа МакДака.

# Khasanova I. F.
# 31.03.2016

import random

print("Программа случайным образом отображает имя одного из трех племянников Скруджа МакДака.")

name = random.randint(1,3)

print('\nИмя одного из племянников Скруджа МакДака '+"-", end=' ')

if name == 1 :
    print('Билли.')
elif name == 2 :
    print('Вилли.')  
else :
    print('Дилли.')


input("\n\nНажмите Enter для выхода.")