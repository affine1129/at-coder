import sys

MAX = 10**9

input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
X_Y = set([tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)])


def bfs(count: int, tar: int, rem: set[int], point: int):
    ret = MAX

    point += A[tar][count]

    if count == (N - 1):
        return point

    for nex in rem:
        if (min(tar, nex), max(tar, nex)) not in X_Y:
            nex_rem = rem.copy()
            nex_rem.remove(nex)
            ret = min(ret, bfs(count + 1, nex, nex_rem, point))

    return ret


ans = MAX
for i in range(N):
    rem = {j for j in range(N)}
    rem.remove(i)
    ans = min(ans, bfs(0, i, rem, 0))

print(-1 if ans == MAX else ans)
