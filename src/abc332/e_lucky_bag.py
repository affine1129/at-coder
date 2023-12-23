import sys

input = sys.stdin.readline

N, D = map(int, input().split())
W = list(map(int, input().split()))

dp = [[float('inf')] * (1 << N) for _ in range(D)]

mean = sum(W) / D
for i in range(1 << N):
    sum_ = 0
    for j in range(N):
        if i & (1 << j):
            sum_ += W[j]
    dp[0][i] = (sum_ - mean) ** 2 / D

for d in range(D-1):
    for i in range(1 << N):
        j = i
        while j > 0:
            j = (j - 1) & i
            dp[d+1][i] = min(dp[d+1][i], dp[d][i-j] + dp[0][j])

print(dp[-1][-1])
