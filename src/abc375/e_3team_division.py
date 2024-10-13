N = int(input())
A, B = zip(*[list(map(int, input().split())) for _ in range(N)])

sum_b = sum(B)
if sum_b % 3 != 0:
    print(-1)
    exit()

MAX = 10 ** 18

s3 = sum_b // 3
dp = [[[MAX] * (s3 + 1) for _ in range(s3 + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0
for i in range(N):
    a, b = A[i], B[i]
    for j in range(s3 + 1):
        for k in range(s3 + 1):
            # team1の場合
            if j + b <= s3:
                dp[i + 1][j + b][k] = min(dp[i + 1][j + b][k], dp[i][j][k] + int(a != 1))
            # team2の場合
            if k + b <= s3:
                dp[i + 1][j][k + b] = min(dp[i + 1][j][k + b], dp[i][j][k] + int(a != 2))
            # team3の場合
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k] + int(a != 3))

print(-1 if dp[-1][s3][s3] == MAX else dp[-1][s3][s3])
