K = int(input())
MOD = 10 ** 9 + 7


if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K + 1)
dp[0] = 1
for i in range(1, K + 1):
    for j in range(1, min(i + 1, 10)):
        dp[i] += dp[i - j]
        dp[i] %= MOD

print(dp[K])
