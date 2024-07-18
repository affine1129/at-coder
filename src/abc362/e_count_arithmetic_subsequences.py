MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

dp = [[[0] * N for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i][0] = 1

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        d = A[j] - A[i]
        for l in range(1, N):
            if l == 1:
                dp[i][j][1] = 1
                continue
            for k in range(j + 1, N):
                if A[k] - A[j] == d:
                    dp[i][j][l] += dp[j][k][l - 1]
                    dp[i][j][l] %= MOD

ans = [0] * N
for i in range(N):
    for j in range(N):
        for l in range(N):
            ans[l] += dp[i][j][l]
            ans[l] %= MOD

print(*ans)
