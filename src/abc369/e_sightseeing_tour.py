import itertools
import sys

input = sys.stdin.readline
MAX = 10 ** 18

N, M = map(int, input().split())
bridges = []
distances = [[MAX] * N for _ in range(N)]
for i in range(N):
    distances[i][i] = 0
for _ in range(M):
    U, V, T = map(int, input().split())
    U -= 1
    V -= 1
    bridges.append((U, V, T))
    distances[U][V] = distances[V][U] = min(distances[U][V], T)

for i in range(N):
    for j in range(N):
        for k in range(N):
            distances[j][k] = min(distances[j][k], distances[j][i] + distances[i][k])

Q = int(input())
for _ in range(Q):
    K = int(input())
    B = set(map(lambda x: int(x) - 1, input().split()))

    ans = MAX
    for b in itertools.permutations(B):
        cur1 = 0
        cur2 = 0
        dp = [[MAX] * 2 for _ in range(K + 1)]
        dp[0][0] = dp[0][1] = 0
        for i, j in enumerate(b):
            u, v, t = bridges[j]
            dp[i + 1][0] = min(dp[i][0] + distances[cur1][u], dp[i][1] + distances[cur2][u]) + t
            dp[i + 1][1] = min(dp[i][0] + distances[cur1][v], dp[i][1] + distances[cur2][v]) + t
            cur1 = v
            cur2 = u
        ans = min(ans, dp[K][0] + distances[cur1][N - 1], dp[K][1] + distances[cur2][N - 1])

    print(ans)
