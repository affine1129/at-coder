import sys

INF = 10 ** 6

input = sys.stdin.readline

N, X, Y = map(int, input().split())
# [何個目の料理か][何個食べたか][甘さ]
dp = [[[INF] * (X + 1) for _ in range(i + 1)] for i in range(N + 1)]

dp[0][0][0] = 0
for i in range(N):
    A, B = map(int, input().split())
    for j in range(i + 1):
        for k in range(X + 1):
            # 食べない場合
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            # 食べる場合
            if k + A <= X:
                sum_ = dp[i][j][k] + B
                if sum_ <= Y:
                    dp[i + 1][j + 1][k + A] = min(dp[i + 1][j + 1][k + A], sum_)

for i in range(N, -1, -1):
    if min(dp[N][i]) != INF:
        print(min(i + 1, N))
        break
