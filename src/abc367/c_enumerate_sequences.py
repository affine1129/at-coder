import copy


N, K = map(int, input().split())

R = list(map(int, input().split()))

list_ = [[r + 1] for r in range(R[0])]
for n in range(1, N):
    tmp = copy.deepcopy(list_)
    list_ = []
    for t in tmp:
        for r in range(R[n]):
            list_.append(t + [r + 1])

for l in list_:
    if sum(l) % K == 0:
        print(*l)
