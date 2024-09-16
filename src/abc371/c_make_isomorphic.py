import itertools
import sys
import copy

input = sys.stdin.readline

N = int(input())

MG = int(input())
graph_g = [set() for _ in range(N)]
for _ in range(MG):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    graph_g[u].add(v)
    graph_g[v].add(u)

MH = int(input())
graph_h = [set() for _ in range(N)]
for _ in range(MH):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph_h[a].add(b)
    graph_h[b].add(a)

A = [list(map(int, input().split())) for _ in range(N - 1)]


def diff(ls_g: list[set[int]], ls_h: list[set[int]]) -> int:
    sum_ = 0
    for i in range(N):
        tar_g = ls_g[i]
        tar_h = ls_h[i]
        if tar_g == tar_h:
            continue

        plus = tar_h - tar_g
        minus = tar_g - tar_h

        for p in plus:
            ls_g[i].add(p)
            ls_g[p].add(i)
            sum_ += A[i][p - i - 1]
        for m in minus:
            ls_g[i].remove(m)
            ls_g[m].remove(i)
            sum_ += A[i][m - i - 1]
    return sum_


def replace(ls: list[set], per: tuple[int]) -> list[set]:
    ret = [set() for _ in range(N)]
    for i, p in enumerate(per):
        tar = ls[i]
        for t in tar:
            ret[p].add(per[t])
    return ret


ans = 10 ** 10
for v in itertools.permutations(range(0, N)):
    ans = min(ans, diff(copy.deepcopy(graph_h), replace(graph_g, v)))

print(ans)
