import sys

input = sys.stdin.readline

N, M = map(int, input().split())
C_P_S = [list(map(int, input().split())) for _ in range(N)]

conv_rouletts = []
for roulett in C_P_S:
    cost, points = roulett[0], roulett[2:]
    if zeros := points.count(0):
        cost *= len(points) / (len(points) - zeros)
        points = [p for p in points if p > 0]
    conv_rouletts.append((cost, points))
    
ans = [1e10] * M
for m in range(M-1, -1, -1):
    for cost, points in conv_rouletts:
        cost_sum = 0
        for p in points:
            if m + p < M:
                cost_sum += ans[m+p]
        ans[m] = min(ans[m], cost_sum / len(points) + cost)

print(ans[0])
