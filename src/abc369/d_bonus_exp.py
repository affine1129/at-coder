N = int(input())
A = list(map(int, input().split()))

# 0: 奇数, 1：偶数
dp = [[0] * 2 for _ in range(N)]
dp[0][0] = A[0]
for i in range(1, N):
    a = A[i]
    dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][0])
    dp[i][1] = max(dp[i - 1][0] + a * 2, dp[i - 1][1])

print(max(dp[-1]))
