# Упражнение 2
# Список L состоит из списков из двух элементов li. Допишите код в клетке снизу так, чтобы li были упорядочены согласно произведениям содержащихся в них элементов.

from random import randint
L = [[randint(-5, 5), randint(-5, 5)] for _ in range(10)]

multiply = lambda l: l[0]*l[1]
sorted_list = sorted(L, key=multiply)
print(sorted_list)
