N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

MAX = 5001
map_ = [[0] * MAX for _ in range(MAX)]

for A, B in AB:
    map_[A][B] += 1

for i in range(MAX):
    for j in range(MAX - 1):
        map_[i][j + 1] += map_[i][j]

for i in range(MAX):
    for j in range(MAX - 1):
        map_[j + 1][i] += map_[j][i]

if K == (MAX - 1):
    print(map_[-1][-1])
    exit()

ans = 0
diff = K + 1
for i in range(diff, MAX):
    for j in range(diff, MAX):
        ans = max(ans, map_[i][j] - map_[i - diff][j] - map_[i][j - diff] + map_[i - diff][j - diff])

print(ans)
