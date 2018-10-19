# Упражнение 4
# Программа сначала получает на вход строку S, а затем натуральное число N. На выходе должна быть такая строка R, что каждый символ из S повторяется N раз.

def multiply(s, n):
    r = ''
    for char in s:
        r = r + char * n
    return r


S = str(input())
N = int(input())
R = multiply(S, N)
print(R)
 
