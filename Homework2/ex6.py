# Упражнение 6
# Напишите программу, заменяющую в подаваемой на вход строке пробелы на запятые, используя при этом методы split() и  join(). Потом сделайте тоже самое с помощью метода replace().

def GetRidOfSpace1(s):
    l = s.split()
    s = ','.join(l)
    return s

def GetRidOfSpace2(s):
    s = s.replace(' ', ',')
    return s

S = str(input())
print(GetRidOfSpace2(S))
print(GetRidOfSpace1(S))
