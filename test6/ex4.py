with open('test6_ex4.txt.', 'a') as f:
    s = str(input())
    if s != 'STOP':
        f.write(s, '\n')
