from collections import defaultdict
from typing import Tuple
import sys

sys.setrecursionlimit(10**6)


N = int(input())
c_sum = 0
graph = defaultdict(list)
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    c_sum += c
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(tar) -> Tuple[int, int]:
    seen[tar] = True
    max_cost = 0
    max_goal = tar
    for next, cost in graph[tar]:
        if seen[next]:
            continue
        goal, cost_sum = dfs(next)
        cost_sum += cost
        if max_cost < cost_sum:
            max_cost = cost_sum
            max_goal = goal
    return max_goal, max_cost


seen = [False] * N
goal, _ = dfs(0)

seen = [False] * N
_, cost = dfs(goal)

ans = c_sum * 2 - cost
print(ans)
