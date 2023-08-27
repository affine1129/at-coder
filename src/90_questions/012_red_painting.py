import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

H, W = map(int, input().split())
Q = int(input())


def dfs(dept, dest, mat, dir=[[0, 1], [0, -1], [1, 0], [-1, 0]]):
    res = 0
    if mat[dept[0]][dept[1]] == 1:
        if dept == dest:
            return True
        for d in dir:
            nex = [dept[0] + d[0], dept[1] + d[1]] 
            if nex[0] > dest[0] or nex[1] > dest[0]:
                continue
            res += dfs(nex, dest, mat)
    return bool(res)

mat = [[0] * W for _ in range(H)]
for _ in range(Q):
    t_r_c = list(map(int, input().split()))
    if t_r_c[0] == 1:
        r, c = map(lambda x: x-1, t_r_c[1:])
        mat[r][c] = 1

    else:
        ra, ca, rb, cb = map(lambda x: x-1, t_r_c[1:])
        ans = False
        # aが右下, bが左上
        if ra > rb and ca > cb:
            ans = dfs([rb, cb], [ra, ca], mat[rb:ra][cb:ca])
        # aが左下, bが右上
        elif ra > rb and cb > ca:
            ans = dfs([H-1-ra, ca], [H-1-rb, cb], mat[::-1])
        # aが右上, bが左下
        elif rb > ra and ca > cb:
            ans = dfs([H-1-rb, cb], [H-1-ra, ca], mat[::-1])
        # その他
        else:
            ans = dfs([ra, ca], [rb, cb], mat)

        if ans:
            print('Yes')
        else:
            print('No')

print(mat)
