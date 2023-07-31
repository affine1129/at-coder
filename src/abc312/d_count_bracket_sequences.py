import numpy as np

MOD = 998244353

S = input()
N = len(S)
half = N // 2

dp = np.array([[0] * (half + 1) for _ in range(N+1)])
dp[0][0] = 1

for i in range(N):
    if S[i] != ')':
        dp[i+1][1:] += dp[i][:-1]
    if S[i] != '(':
        dp[i+1][:-1] += dp[i][1:]
    dp[i+1] %= MOD

print(dp[N][0])

