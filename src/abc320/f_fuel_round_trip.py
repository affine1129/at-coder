import sys

input = sys.stdin.readline

N, H = map(int, input().split())
X = [0] + list(map(int, input().split()))
P_F = [list(map(int, input().split())) for _ in range(N-1)] + [[0, 0]]

H1 = H+1
INF = 10 ** 18

# dp[距離][往路でのガソリン残][復路でのガソリン残]
dp = [[[INF] * H1 for _ in range(H1)] for _ in range(N+1)]
for i in range(H1):
    dp[0][H][i] = 0

for i in range(0, N):
    d = X[i+1] - X[i]
    p, f = P_F[i]
    # jを往路のi地点での給油した後のガソリン量
    for j in range(0, H1): 
        # kを復路のi地点での給油する前のガソリン量
        for k in range(0, H1):
            if dp[i][j][k] == INF or j-d < 0 or k+d > H:
                continue

            # 行きで給油する場合
            #  dp[i+1][min(j+f, H)-d][k+d] = min(dp[i+1][min(j+f, H)-d][k+d], dp[i][min(j+f, H)][k] + p)
            if j+f-d > H:
                dp[i+1][H][k+d] = min(dp[i+1][H][k+d], dp[i][j][k] + p)
            else:
                dp[i+1][j+f-d][k+d] = min(dp[i+1][j+f-d][k+d], dp[i][j][k] + p)

            # 給油しない場合
            dp[i+1][j-d][k+d] = min(dp[i+1][j-d][k+d], dp[i][j][k])

            # 帰りに給油する場合
            if k + d == H:
                for l in range(f+1):
                    dp[i+1][j-d][H-l] = min(dp[i+1][j-d][H-l], dp[i][j][k] + p)
            else:
                dp[i+1][j-d][k+d-f] = min(dp[i+1][j-d][k+d-f], dp[i][j][k] + p)

ans = min([dp[-1][j][j] for j in range(H1)])
print(-1 if ans==INF else ans)
