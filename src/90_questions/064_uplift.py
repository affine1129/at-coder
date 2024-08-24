N, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
diff = [0] * (N - 1)
for i in range(0, N - 1):
    tmp = A[i + 1] - A[i]
    diff[i] = tmp
    ans += abs(tmp)

for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 2
    R -= 1

    pre = 0
    nex = 0
    if L != -1:
        pre += abs(diff[L])
        diff[L] += V
        nex += abs(diff[L])
    if R != (N - 1):
        pre += abs(diff[R])
        diff[R] -= V
        nex += abs(diff[R])

    ans -= pre - nex
    print(ans)
