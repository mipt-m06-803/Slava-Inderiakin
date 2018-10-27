A = ['a', 'b', 'c', 'd', 'U']
B = ['e', 'f', 'g', 'h', 'U']
C = ['e', 'f', 'g', 'h', 'U']
D = ['1', '2', '3', '4', '5']

i = 0

for el0, el1, el2, el3 in zip(A,B,C,D):
    if i == 0:
        a = [el0, el1, el2, el3]
    if i == 1:
        b = [el0, el1, el2, el3]
    if i == 2:
        c = [el0, el1, el2, el3]
    if i == 3:
        d = [el0, el1, el2, el3]
    if i == 4:
         e = [el0, el1, el2, el3]
    i += 1

print(a, b, c, d, e)
