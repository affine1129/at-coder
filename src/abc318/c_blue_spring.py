import sys

input = sys.stdin.readline

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)

dp = [ ((i-1) // D + 1) * P for i in range(N+1)] 
dp[0] = 0

for i in range(N):
    dp[i+1] = min(dp[i] + F[i], dp[i+1])

print(dp[N])
