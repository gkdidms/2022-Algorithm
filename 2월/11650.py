
import sys
input = sys.stdin.readline
n = int(input())
xylist = []
for i in range(n):
    m = list(map(int, input().split()))
    xylist.append(m)

xylist.sort(key=lambda x: (x[0],x[1]))
for j in range(n):
    print(str(xylist[j][0]) + " " + str(xylist[j][1]))