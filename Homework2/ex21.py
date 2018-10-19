# Упражнение 21
# На вход программе подаются несколько чисел, разделенных пробелами. Отсортируйте эти числа по убыванию используя алгоритм сортировки выбором. Не используйте встроенные инструменты python для сортировки (функцию sorted() и метод sort() объектов типа list). Распечатайте список с упорядоченными числами.

def SelectionSort(l):
    for k in range(len(l) - 1):
        m = k
        i = k + 1
        while i < len(l):
            if l[i] < l[m]:
                m = i
            i += 1
        t = l[k]
        l[k] = l[m]
        l[m] = t
    return(l)

def Read(s):
    l = [float(el) for el in s.split(' ')]
    return(l)

S = str(input())
L = Read(S)
L = SelectionSort(L)
print(L)
