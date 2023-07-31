import sys

input = sys.stdin.readline

N = int(input())
# 小立方体が入っている立方体番号を格納する
list_ = [[[-1] * 101 for _ in range(101)] for _ in range(101)]
for i in range(N):
    x0, y0, z0, x1, y1, z1 = map(int, input().split())
    set_ = set()
    for x in range(x0, x1):
        for y in range(y0, y1):
            for z in range(z0, z1):
                list_[x][y][z] = i

ans = [set() for _ in range(N)]
for x in range(101):
    for y in range(101):
        for z in range(101):
            if list_[x][y][z] == -1:
                continue
            if list_[x][y][z] != list_[x+1][y][z] and list_[x+1][y][z] != -1:
                ans[list_[x][y][z]].add(list_[x+1][y][z])
                ans[list_[x+1][y][z]].add(list_[x][y][z])
            if list_[x][y][z] != list_[x][y+1][z] and list_[x][y+1][z] != -1 :
                ans[list_[x][y][z]].add(list_[x][y+1][z])
                ans[list_[x][y+1][z]].add(list_[x][y][z])
            if list_[x][y][z] != list_[x][y][z+1] and list_[x][y][z+1] != -1:
                ans[list_[x][y][z]].add(list_[x][y][z+1])
                ans[list_[x][y][z+1]].add(list_[x][y][z])

print('\n'.join(map(lambda x: str(len(x)), ans)))
