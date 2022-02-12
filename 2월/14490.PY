from math import gcd


n,m = map(int, input().split(':'))

NMgcd = gcd(n,m)
n = str(n//NMgcd)
m = str(m//NMgcd)

print(n+":"+m)