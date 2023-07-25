import sys

input = sys.stdin.readline

H, W, N = map(int, input().split())
A_B_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[1] * W for _ in range(H)]
for a_b in A_B_list:
    dp[a_b[0]-1][a_b[1]-1] = 0

for i in range(1, H):
    for j in range(1, W):
        if dp[i][j] == 0:
            continue

        dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1

print(sum([sum(res) for res in dp]))
