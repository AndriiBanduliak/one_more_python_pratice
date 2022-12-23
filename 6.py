'''Pеализовать два небольших скрипта:
* итератор, генерирующий целые числа, начиная с указанного;
* итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения. 
Например, в первом задании выводим целые числа, начиная с 3. 
При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть 
условие, при котором повторение элементов списка прекратится'''

from itertools import islice, cycle, count


def unexpected(start_el, stop_el, num_str):
    try:
        start_el, stop_el, num_str = int(start_el), int(stop_el), int(num_str)
        my_list = [el for el in islice(count(), start_el, stop_el + 1)]
        r_list = iter(el for el in cycle(my_list))
        repear_list = [next(r_list) for _ in range(num_str)]
        print(my_list)
        return repear_list
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"