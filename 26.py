'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''
def Power(A, B):
    if B>0:
        return A * Power(A, B-1)
    else:
        return 1


print('Введите число: ')
A = int (input ())
print('Введите степень: ')
B = int (input ())

res = Power(A, B)
print(res)