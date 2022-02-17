
n = input().split(' ')
for i in n:
    if i == '':
        n.remove('')
if n[0] == '' and len(n) == 1:
    print(0)
else:
    print(len(n))