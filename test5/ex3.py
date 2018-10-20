# Задача 3
# Замените 3 выражения в теле цикла одним множественным присваиванием.

def trib(n):
    if n < 4:
        return 1
    trib1, trib2, trib3 = 1, 1, 1
    for _ in range(n - 3):
        trib3, trib2, trib1 = trib1 + trib2 + trib3, trib3 - trib1 - trib2, trib3 - trib1 - trib2
    return trib3

for i in range(1, 20):
    print(trib(i))
