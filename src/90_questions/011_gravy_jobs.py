import sys
import numpy as np

input = sys.stdin.readline

N = int(input())
D_C_S = [list(map(int, input().split())) for _ in range(N)]
D_C_S.sort(key=lambda x: x[0])

dp = np.zeros(5001, dtype=np.int64)

for d, c, s in D_C_S:
    if c <= d:
        dp[c:d+1] = np.maximum(dp[c:d+1], dp[:d+1-c] + s)

print(max(dp))
