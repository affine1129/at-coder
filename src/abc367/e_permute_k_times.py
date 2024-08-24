N, K = map(int, input().split())
X = list(map(lambda x: int(x) - 1, input().split()))
A = list(map(int, input().split()))


def exec(k):
    if k == 0:
        return [i for i in range(N)]
    elif k % 2 == 0:
        y = exec(k // 2)
        return [y[v] for v in y]
    else:
        y = exec(k - 1)
        return [y[v] for v in X]


res = exec(K)
print(*[A[v] for v in res])
