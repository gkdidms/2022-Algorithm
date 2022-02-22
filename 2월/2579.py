# n = int(input())
# stairs = [0]* n
# stairsData = [0]*n
# i = 0
# sum = 0
# for j in range(n):
#     stairs[j] = int(input())


# while n > i :
#     if i == 0:
#         sum += stairs[i]
#         stairsData[i] += 1

#     if i == n-2:
#         stairsData[i] = stairsData[i-1] + 1
#         sum += stairs[i+1]
#         i += 1
#         break

#     if stairs[i] + stairs[i+1] > stairs[i] + stairs[i+2]:
#         if i > 0 and stairsData[i] == 2:
#             stairsData[i+2] += 1
#             sum += stairs[i+2]
#             i += 2
#         elif i == n-3 and stairsData[i] == 1:
#             stairsData[i+2] += 1
#             sum += stairs[i+2]
#             i += 2
#         else:
#             stairsData[i+1] = stairsData[i] + 1
#             sum += stairs[i+1]
#             i += 1
#     else:
#         stairsData[i+2] += 1
#         sum += stairs[i+2]
#         i += 2

# print(stairsData)
# print(sum)

import sys


n = int(sys.stdin.readline())
s = [0] * n
dp = [0] * n

for i in range(n):
    s[i] = int(sys.stdin.readline())

if n == 1:
    print(s[0])
elif n == 2:
    print( s[0] + s[1])
else :
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[1] + s[2], s[0] + s[2])
    for i in range(3,n):
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

    print(dp[n-1])