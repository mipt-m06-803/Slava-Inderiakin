# Упражнение 1
# Напишите программу, которая переставляет в обратном порядке символы второй половины строки

def inversia(s):
    if len(s) < 2:
        return None
    else:
        s1 = s[: len(s)//2]
        s2 = s[: len(s)//2 - 1 : -1]
        s = s1 + s2
        return (s)

a = str(input())
print(inversia(a))
