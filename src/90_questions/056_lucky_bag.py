N, S = map(int, input().split())

A_B = [tuple(map(int, input().split())) for _ in range(N)]

MAX = 10 ** 5 + 1

dp = [[False] * MAX for _ in range(N + 1)]
dp[0][0] = True
for n in range(N):
    a, b = A_B[n]
    for i in range(MAX):
        if dp[n][i]:
            if i + a <= S:
                dp[n + 1][i + a] = True
            if i + b <= S:
                dp[n + 1][i + b] = True

ans = ''
if dp[N][S]:
    cur = S
    for i in range(N - 1, -1, -1):
        a, b = A_B[i]
        if dp[i][cur - a]:
            ans = 'A' + ans
            cur -= a
        elif dp[i][cur - b]:
            ans = 'B' + ans
            cur -= b
        else:
            raise Exception
else:
    ans = 'Impossible'

print(ans)
