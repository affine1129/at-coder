N = int(input())
S = input()

# 0: o, 1: x, 2: ox
dp = [[0] * 3 for _ in range(N + 1)]
ans = 0
for i in range(N):
    s = S[i]
    if s == 'o':
        dp[i + 1][0] = dp[i][0] + 1
        dp[i + 1][1] = 0
        dp[i + 1][2] = dp[i][1] + dp[i][2]
        ans += dp[i][1] + dp[i][2]
    else:
        dp[i + 1][0] = 0
        dp[i + 1][1] = dp[i][1] + 1
        dp[i + 1][2] = dp[i][0] + dp[i][2]
        ans += dp[i][0] + dp[i][2]

print(ans)
