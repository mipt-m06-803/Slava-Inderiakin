# Упражнение 7
# Программа должна считывать 2 строки и проверять, входит ли вторая строка в первую. На выходе должно быть True или False

def Check(s1, s2):
    return s2 in s1

S1 = str(input())
S2 = str(input())
print(Check(S1, S2))
