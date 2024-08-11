import sys

input = sys.stdin.readline

N = int(input())
A = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]

a = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            a[x][y][z] += A[x - 1][y - 1][z - 1]
            a[x][y][z] += a[x][y][z - 1]
            a[x][y][z] += a[x][y - 1][z]
            a[x][y][z] += a[x - 1][y][z]
            a[x][y][z] -= a[x][y - 1][z - 1]
            a[x][y][z] -= a[x - 1][y - 1][z]
            a[x][y][z] -= a[x - 1][y][z - 1]
            a[x][y][z] += a[x - 1][y - 1][z - 1]


Q = int(input())
for _ in range(Q):
    ans = 0
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    lx -= 1
    #  rx -= 1
    ly -= 1
    #  ry -= 1
    lz -= 1
    #  rz -= 1
    ans += a[rx][ry][rz]
    ans -= a[lx][ry][rz]
    ans -= a[rx][ly][rz]
    ans -= a[rx][ry][lz]
    ans += a[lx][ly][rz]
    ans += a[rx][ly][lz]
    ans += a[lx][ry][lz]
    ans -= a[lx][ly][lz]
    print(ans)
