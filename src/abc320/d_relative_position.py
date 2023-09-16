import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

ts = [[] for _ in range(N)]
for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A, B = A-1, B-1
    ts[A].append((B, X, Y))
    ts[B].append((A, -X, -Y))

q = [0]
set_ = {i for i in range(1, N)}
loc = [[10**19, 10**19] for _ in range(N)]
loc[0] = [0, 0]
while len(q) > 0:
    i1 = heapq.heappop(q)
    for t in ts[i1]:
        if t[0] in set_: 
            i2 = t[0]
            heapq.heappush(q, i2)
            loc[i2] = [loc[i1][0] + t[1], loc[i1][1] + t[2]]
            set_.remove(i2)

print(0, 0)
for l in loc[1:]:
    if l == [10**19, 10**19]:
        print('undecidable')
    else:
        print(*l)
