N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def check(num: int) -> int:
    a = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tar = A[i][j]
            a[i][j] = num if tar == -1 else tar

    for i in range(N):
        for j in range(N):
            for k in range(N):
                a[j][k] = min(a[j][k], a[j][i] + a[i][k])

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if i == j:
                continue
            ans += int(a[i][j] <= P)

    return ans


def search(num: int) -> int:
    r = P + 1
    l = 0
    while l + 1 < r:
        mid = (l + r) // 2
        ret = check(mid)
        if ret >= num:
            l = mid
        else:
            r = mid
    return l


max_ = check(P + 1)
min_ = check(0)
if max_ == K:
    print('Infinity')
    exit()

if min_ < K or K < max_:
    print(0)
    exit()

print(search(K) - search(K + 1))
