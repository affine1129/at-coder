N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]
lr_range = [range(l - 1, r) for l, r in LR]

MAX = 100

ans = 0
for i in range(N):
    L1, R1 = LR[i]
    L1 -= 1
    for j in range(i + 1, N):
        L2, R2 = LR[j]
        L2 -= 1
        tmp = 0
        for k in range(L1, R1):
            tmp += len(list(filter(lambda x: x < k, lr_range[j])))
        ans += tmp / ((R1 - L1) * (R2 - L2))

print(ans)
