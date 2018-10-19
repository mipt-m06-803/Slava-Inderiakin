# Упражнение 20
# Допишите код в следуещей клетке так, чтобы элементы двумерного массива A были возведены в квадрат.

import random
num_rows = 6
num_columns = 7
A = [[random.randint(-10, 10) for _ in range(num_columns)] for _ in range(num_rows)]  # random.randint(a, b) возвращает случайное целое число от a до b
# Нижнее подчеркивание _ имеет несколько назначений в python
# Одно из них - отбрасывать результаты операций, который не нужны в программе

for elem in A:
    for i in range(num_columns):
        elem[i] = elem[i] ** 2

print(A)
