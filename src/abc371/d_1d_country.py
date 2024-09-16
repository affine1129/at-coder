import bisect

DIFF = 10 ** 9

N = int(input())
X = list(map(lambda x: int(x) + DIFF, input().split()))
P = list(map(int, input().split()))
Q = int(input())

ls_p = [0] * N
ls_x = [0] * N
for i in range(N):
    ls_p[i] = P[i] + ls_p[i - 1]
    ls_x[i] = X[i]

for _ in range(Q):
    L, R = map(int, input().split())
    L, R = L + DIFF, R + DIFF
    il = bisect.bisect_left(ls_x, L)
    ir = bisect.bisect_right(ls_x, R)

    left = ls_p[il - 1] if il != 0 else 0
    right = 0 if ir == 0 else ls_p[ir - 1] if ir != N else ls_p[-1]
    print(right - left)
