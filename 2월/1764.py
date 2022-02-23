import sys

n,m = map(int, sys.stdin.readline().split())
list1 = [0]*n
list2 = [0]*m
sumDict = {}
sumList = []
for i in range(n):
    name = sys.stdin.readline()
    sumDict[name] = 1

for j in range(m):
    name = sys.stdin.readline()
    sumDict[name] = sumDict.get(name, 0) + 1 

for key, value in sumDict.items():
    if value == 2:
        sumList.append(key)

sumList.sort()
print(len(sumList))

answer = ""
for q in sumList:
    answer += q
print(answer)