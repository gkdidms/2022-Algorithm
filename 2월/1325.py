import sys
from collections import defaultdict, deque

input = sys.stdin.readline

arr = defaultdict(list)
n,m = map(int, input().split())

for _ in range(m):
    s,e = map(int, input().split())
    arr[e].append(s)

def bfs(x):
    visited = [False]*(n+1)
    visited[x] = True
    queue = deque([x])
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                cnt+=1
                queue.append(i)
    return cnt

_max = 0
answer = []
for i in range(1, n+1):
    result = bfs(i)
    if result > _max:
        _max = result
        answer = [i]
    elif result == _max:
        answer.append(i)

print(*answer)


