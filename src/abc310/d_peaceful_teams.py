import sys

input = sys.stdin.readline

N, T, M = map(int, input().split())

d_list = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    d_list[a].add(b)
    d_list[b].add(a)

teams = [[] for _ in range(T)]

def dfs(mem_num):
    res = 0

    if mem_num == N:
        return all(teams)

    for team in teams:
        for p in team:
            if p in d_list[mem_num]: break
        else:
            team.append(mem_num)
            res += dfs(mem_num + 1)
            team.pop()
            if len(team) == 0:
                break

    return res

print(dfs(0))
