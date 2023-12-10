N, M = map(int, input().split())
A = list(map(int, input().split()))

ls = [0] * (N+1)
max_ = 0
for a in A:
    ls[a] += 1
    cur = ls[a]
    pre = ls[max_]
    if a != max_:
        max_ = a if cur > pre else max_ if cur < pre else max_ if a > max_ else a
    print(max_)
