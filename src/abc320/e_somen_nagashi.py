import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

p = [0 for _ in range(N)]
s = [i for i in range(N)]
q = []
for _ in range(M):
    T, W, S = map(int, input().split())
    heapq.heappush(q, (T, 1, W, S))

while len(q) > 0:
    pop = heapq.heappop(q)

    if pop[1] == 0:
        heapq.heappush(s, pop[2])
    else:
        if len(s) == 0:
            continue
        t = heapq.heappop(s)
        heapq.heappush(q, (pop[0]+pop[3], 0, t))
        p[t] += pop[2]
        
[print(i) for i in p]
