import sys

input = sys.stdin.readline


sys.setrecursionlimit(10**6)


N = int(input())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

seen = [False] * N
list_ = [0] * N


def dfs(node: int) -> int:
    num = 1
    seen[node] = True
    tars = graph[node]
    for tar in tars:
        if seen[tar]:
            continue
        num += dfs(tar)
    list_[node] = (N - num) * num
    return num


dfs(0)
print(sum(list_))
