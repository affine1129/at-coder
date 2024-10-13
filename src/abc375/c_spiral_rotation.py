N = int(input())
A = [list(input()) for _ in range(N)]

ans = [[''] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        num = min(i + 1, j + 1, N - i, N - j)
        tar_x, tar_y = i, j
        for _ in range(num % 4):
            tar_x, tar_y = tar_y, N - 1 - tar_x
        ans[tar_x][tar_y] = A[i][j]

[print(''.join(a)) for a in ans]
