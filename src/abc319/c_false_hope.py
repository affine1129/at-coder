import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


C = [list(map(int, input().split())) for _ in range(3)]

sum_ = 362880

ng = []
for i in range(3):
    if C[i][0] == C[i][1]:
        ng.append(({i*3, i*3+1}, {i*3+2}))
    elif C[i][1] == C[i][2]:
        ng.append(({i*3+1, i*3+2}, {i*3}))
    elif C[i][2] == C[i][0]:
        ng.append(({i*3+2, i*3}, {i*3+1}))
    if C[0][i] == C[1][i]:
        ng.append(({i, i+3}, {i+6}))
    elif C[1][i] == C[2][i]:
        ng.append(({i+3, i+6}, {i}))
    elif C[2][i] == C[0][i]:
        ng.append(({i+6, i}, {i+3}))
if C[0][0] == C[1][1]:
    ng.append(({0, 4}, {8}))
elif C[1][1] == C[2][2]:
    ng.append(({4, 8}, {0}))
elif C[2][2] == C[0][0]:
    ng.append(({8, 0}, {4}))
if C[0][2] == C[1][1]:
    ng.append(({2, 4}, {6}))
elif C[1][1] == C[2][0]:
    ng.append(({4, 6}, {2}))
elif C[2][0] == C[0][2]:
    ng.append(({6, 2}, {4}))

set_ = {i for i in range(9)}
def dfs(x, selected):
    ret = 0
    selected.add(x)

    if len(selected) == 9:
        return 1

    for n in ng:
        if n[0] <= selected and not n[1] <= selected:
            return 0

    for i in (set_ - selected):
        ret += dfs(i, selected)
        selected.remove(i)

    return ret

count = 0
for i in range(9):
    count += dfs(i, set())

print(count/sum_)
