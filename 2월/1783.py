n ,m = map(int, input().split())
answer = 0
if n == 1 :
    answer = 1
elif n == 2:
    answer = min(4, (m-1)//2+1)
elif m <=6:
    answer = min(4, m)
else :
    answer = m - 2

print(answer)    