# Упражнение 7
# Сформируйте кортеж t2 из строк, находящихся в кортеже t, длина которых больше 5.

from random import randint
t = tuple(
    [
        ''.join(
            [chr(ord('а') + randint(0, 32)) for _ in range(randint(0, 10))]
        ) for _ in range(randint(5, 15))
    ]
)
print(t)

t2 = tuple(el for el in t if len(el) > 4)
print(t2)
