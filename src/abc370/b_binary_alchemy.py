N = int(input())
A = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

cur = 0
for i in range(N):
    if cur <= i:
        cur = A[i][cur]
    else:
        cur = A[cur][i]

print(cur + 1)
