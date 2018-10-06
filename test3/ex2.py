str1 = str(input())
N = len(str1)
str2 = [0] * N
for i in range (N):
    str2[i] = str1[N-1-i]
str2 = str(str2)
if str1 == str2:
    print(str(str1))
else:
    print(str1+str(str2))
