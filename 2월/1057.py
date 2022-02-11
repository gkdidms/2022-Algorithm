

totalNum, n, m = map(int,input().split(' '))
count = 0

while n != m:
    n -= n//2
    m -= m//2
    count += 1

print(count)
    
