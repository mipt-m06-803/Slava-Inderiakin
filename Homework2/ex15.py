# Упражнение 15
# На вход подается строка, расположите символы в строке по убыванию их номера в UNICODE. Используются строковые методы split() и join() и метод  sort() для списков.

def getorder(letter):
    return(ord(letter))

s = input()
l = [substr for substr in s]
l.sort(key = getorder)
print(''.join(l))
