# Упражнение 15
# В следующей клетке задан список l. Напишите цикл while, в теле которого будет удаляться 0-й элемент списка l. Цикл должен прерваться, когда список станет пустым. Использовать список в качестве условия: if l

import random
l = [0]*random.randint(0, 40)

while l:
    del l[0]
print(l)
