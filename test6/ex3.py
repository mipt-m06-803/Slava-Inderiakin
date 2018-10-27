a = set(str(input()))
b = set(str(input()))
c = set(str(input()))

union2 = ((a & b) | (c & b) |(a & c)) - a & b & c
print(union2)
