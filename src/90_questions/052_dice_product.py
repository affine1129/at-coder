import sys

input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

MOD = 10 ** 9 + 7

ans = 1
for n in range(N):
    tmp = 0
    for i in range(6):
        tmp += A[n][i] * ans
        tmp %= MOD
    ans = tmp
    ans %= MOD

print(ans)
