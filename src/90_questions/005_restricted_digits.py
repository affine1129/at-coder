N, B, K = map(int, input().split())

c_list = list(map(int, input().split()))

dp = [[0 for _ in range(B)] for _ in range(N)]

for n in range(N):
    if n == 0:
        for c in c_list:
            dp[n][c % B] += 1 
    else:
        for b in range(B):
            for c in c_list:
                dp[n][(c * 10 ** n + b) % B] += dp[n-1][b] 

print(dp[N-1][0])

         
