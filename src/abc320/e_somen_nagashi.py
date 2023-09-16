import sys

input = sys.stdin.readline

N, M = map(int, input().split())

bp = [0] * N
p = [0] * N
for _ in range(M):
    T, W, S = map(int, input().split())
    for i in range(len(bp)):
        if bp[i] <= T:
            p[i] += W
            bp[i] = T + S
            break

for ans in p:
    print(ans)
