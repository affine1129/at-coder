N, K = map(int, input().split())

N1 = N + 1

dp = [0] * N1

for i in range(2, N1):
    if dp[i] == 0:
        for j in range(i, N1, i):
            dp[j] += 1

ans = 0
for i, d in enumerate(dp):
    if d >= K:
        ans += 1

print(ans)
