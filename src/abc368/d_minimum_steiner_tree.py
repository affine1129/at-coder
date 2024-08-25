import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

V = list(map(int, input().split()))
init = V[0]
V = set(V)


def dfs(cur: int, par: int) -> int:
    path = 0
    for nex in tree[cur]:
        if nex == par:
            continue

        path += dfs(nex, cur)

    path += (cur in V or path > 0)

    return path


print(dfs(init, 0))
