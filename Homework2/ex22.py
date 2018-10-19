# Упражнение 22
# На вход программе подается строка, сотоящая из слов, разделенных пробелами. Сформируйте список из этих слов, в котором они будут расположены в алфавитном порядке. Предварительно замените прописные буквы строчными с помощью метода lowercase() объектов типа str. Используйте метод сортировки пузырьком.

def BubbleSort(l):
    for n in range (len(l)):
        for i in range(len(l) - n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        n += 1
    return(l)

def Read(s):
    l = [el.lower() for el in s.split()]
    return(l)

S = str(input())
L = Read(S)
print(L)
L = BubbleSort(L)
print(L)
