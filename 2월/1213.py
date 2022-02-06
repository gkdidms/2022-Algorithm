
import sys
from collections import Counter

str = list(map(str, sys.stdin.readline().strip()))
str.sort()
check = Counter(str)

cnt = 0
center = ""

for i in check:
    if check[i] % 2 != 0:
        cnt += 1
        center += i
        str.remove(i)

    if cnt > 1:
        break

if cnt > 1:
    print("I'm Sorry Hansoo")
else :
    res = ""
    for i in range(0, len(str), 2):
        res += str[i]

    print(res + center + res[::-1])

    

        



