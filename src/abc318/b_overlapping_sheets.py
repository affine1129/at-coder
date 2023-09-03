import sys

input = sys.stdin.readline

N = int(input())

mat = [[0] * 101 for _ in range(101)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            mat[i][j] = 1

ans = sum([sum(m) for m in mat])
print(ans)
