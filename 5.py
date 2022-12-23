'''Реализовать формирование списка, используя функцию range() и 
возможности генератора. В список должны войти чётные числа от 100 до 1000 
(включая границы). Нужно получить результат вычисления произведения 
всех элементов списка.
Подсказка: использовать функцию reduce().'''

from functools import reduce


def mul_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(2, 13, 2)]
print(f"list\n{uniq_list}\nMultiplaction of numbers\n{reduce(mul_list,uniq_list)}")