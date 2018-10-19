# Упражнение 3
# Найти самое длинное слово во введенном предложении.

def find(s):
    s = s.replace(',', ' ')             # заменяем запятые
    s = s.replace('.', ' ')             # заменяем точки
    l = s.split()                       # дробим строку на слова

    a = ''                             # создаем переменную под самое длинное слово
    for i in range(len(l)):
        if len(l[i]) > len(a):
            a = l[i]
    return(a)


x = str(input())
print(find(x))
 
