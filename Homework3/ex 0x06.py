# Упражнение 6
# Напишите функцию eat_cookie(), которая печатает строку "What a tasty cookie!". В программе должна быть глобальная переменная NUM_COOKIES_LEFT, которая уменьшается на 1 при каждом вызове eat_cookie(). Если NUM_COOKIES_LEFT <= 0, то функция eat_cookie() должна печатать строку "No more cookies left :(".


def eat_cookie():
    global NUM_COOKIES_LEFT
    if NUM_COOKIES_LEFT > 0:
        NUM_COOKIES_LEFT -= 1
        print("What a tasty cookie!")
    else:
        print("No more cookies left :(")
    return(None)
