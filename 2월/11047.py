n, m = map(int, input().split())

monylist = [0]*n
count = 0
for i in range(n):
    monylist[i] = int(input())

monylist.reverse()

for i in  monylist:
        count += m//i
        m %= i
print(count)
            