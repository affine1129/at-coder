import sys

input = sys.stdin.readline

INF = 10 ** 9
N = int(input())
A = list(map(int, input().split()))
N2 = 2 * N

dp = [[0] * (N2) for _ in range(N2)]

for i in range(N2 - 1):
    dp[i][i + 1] = abs(A[i] - A[i + 1])

for d in range(3, N2, 2):
    for l in range(N2 - d):
        tmp = dp[l + 1][l + d - 1] + abs(A[l] - A[l + d])
        for m in range(l + 1, l + d, 2):
            tmp = min(tmp, dp[l][m] + dp[m + 1][l + d])
        dp[l][l + d] = tmp
print(dp[0][N2 - 1])
