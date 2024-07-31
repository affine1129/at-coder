N = int(input())
MAX = 1001

list_ = [[0] * MAX for _ in range(MAX)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    list_[lx][ly] += 1
    list_[rx][ly] -= 1
    list_[lx][ry] -= 1
    list_[rx][ry] += 1

for i in range(MAX):
    for j in range(MAX - 1):
        list_[i][j + 1] += list_[i][j]

for i in range(MAX):
    for j in range(MAX - 1):
        list_[j + 1][i] += list_[j][i]

ans = [0] * N
for l1 in list_:
    for l in l1:
        if l != 0:
            ans[l - 1] += 1

print(*ans, sep='\n')
