import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

S_list = [input() for _ in range(N)]

d = [[0] * M for _ in range(N)]

def dfs(loc1, loc2, dir):
    while S_list[loc1 + dir[0]][loc2 + dir[1]] == '.':
        d[loc1][loc2] = 1
        loc1 += dir[0]
        loc2 += dir[1]
    if d[loc1][loc2] == 1:
        return
    else:
        d[loc1][loc2] = 1
        if dir == [1, 0] or dir == [-1, 0]:
            dfs(loc1, loc2, [0, 1])
            dfs(loc1, loc2, [0, -1])
        else:
            dfs(loc1, loc2, [1, 0])
            dfs(loc1, loc2, [-1, 0])
        return

for dir in [[1, 0], [0, 1]]:
    dfs(1, 1, dir)

print(sum([sum(res) for res in d]))

