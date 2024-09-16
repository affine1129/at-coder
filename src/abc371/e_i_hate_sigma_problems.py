N = int(input())
A = list(map(int, input().split()))

pos = [[] for _ in range(N + 1)]
for i, a in enumerate(A):
    pos[a].append(i + 1)

ans = 0
for i in range(1, N + 1):
    tmp = [0] + pos[i] + [N + 1]
    cnt = N * (N + 1) // 2
    for j in range(1, len(tmp)):
        d = (tmp[j] - 1) - tmp[j - 1]
        cnt -= d * (d + 1) // 2
    ans += cnt

print(ans)
