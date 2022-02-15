
n = int(input())
numList = []

for i in range(n):
    m = int(input())
    if m == 0:
        numList.pop()
    else:
        numList.append(m)

print(sum(numList))