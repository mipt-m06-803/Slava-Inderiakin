# Упражнение 8
# Напишите программу для заполнения персональной карточки, реализованной в виде словаря. На вход программе последовательно подаются строки из двух слов, разделенных пробелом: первое - название поля в карточке, второе - значение. Заполнение карточки завершается введением строки "STOP".

personal_card = {}

while True:
    InStr = input()
    if InStr == "STOP":
        break
    else:
        l = InStr.split()
        personal_card[l[0]] = l[1]
        print(l)

print(personal_card)
