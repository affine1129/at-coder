import sys

input = sys.stdin.readline

H, W = map(int, input().split())
Si, Sj = map(int, input().split())

grid = []
for _ in range(H):
    C = input()
    grid.append(list(C))

X = input()

cur = (Si - 1, Sj - 1)
for x in X:
    if x == 'L':
        shift = cur[1] - 1
        if shift >= 0 and grid[cur[0]][shift] == '.':
            cur = (cur[0], shift)
    elif x == 'R':
        shift = cur[1] + 1
        if shift < W and grid[cur[0]][shift] == '.':
            cur = (cur[0], shift)
    elif x == 'U':
        shift = cur[0] - 1
        if shift >= 0 and grid[shift][cur[1]] == '.':
            cur = (shift, cur[1])
    elif x == 'D':
        shift = cur[0] + 1
        if shift < H and grid[shift][cur[1]] == '.':
            cur = (shift, cur[1])

print(*map(lambda x: x + 1, cur))
