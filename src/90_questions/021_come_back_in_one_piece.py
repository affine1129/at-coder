import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
scc = []
graph: list[list[int]] = [[] for _ in range(M)]
rev_graph: list[list[int]] = [[] for _ in range(M)]
lifo = deque([])

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    rev_graph[b].append(a)


def dfs(index: int, graph: list[list[int]]) -> int:
    num = lifo.pop()
    seen[num] = True
    for g in graph[num]:
        if not seen[g]:
            lifo.append(g)
            index = dfs(index, graph) + 1
            ret[g] = index
    return index


#  def dfs2() -> None:
#      num = lifo.pop()
#      seen[num] = True
#      for g in graph[num]:
#          if not seen[g]:
#              lifo.append(g)
#              index = dfs(index) + 1
#              ret[g] = index
#      return index


ret = [0 for _ in range(M)]
seen = [False] * M
while tmp := seen.index(False):
    lifo.append(tmp)
    dfs(0, graph)

seen = [False] * M
while tmp := (M - list(reversed(seen)).index(False)):
    lifo.append(ret.index(M - 1))
    dfs(0)
