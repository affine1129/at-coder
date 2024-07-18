import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int, input().split())
    U -= 1
    V -= 1
    graph[U].append((V, B))
    graph[V].append((U, B))

dp = [INF] * N
seen = [False] * N

dp[0] = A[0]
q = [(A[0], 0)]
heapq.heapify(q)

tar = 0
while q:
    cost, tar = heapq.heappop(q)
    if seen[tar]:
        continue
    min_ = INF
    for t in graph[tar]:
        nex_num, nex_cost = t
        if seen[nex_num]:
            continue
        dp[nex_num] = min(dp[nex_num], dp[tar] + nex_cost + A[nex_num])
        heapq.heappush(q, (dp[nex_num], nex_num))
    seen[tar] = True

print(' '.join(map(str, dp[1:])))
