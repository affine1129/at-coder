N, M, X = map(int, input().split())
A, B, S, T = zip(*[list(map(int, input().split())) for _ in range(M)])

event = sorted([(S[i], 1, i) for i in range(M)] + [(T[i], 0, i) for i in range(M)])

ans = [0] * M
ans[0] = X
arrive = [0] * (N + 1)
for v, t, i in event:
    if t == 1 and i != 0:
        ans[i] = max(arrive[A[i]] - v, 0)

    elif t == 0:
        arrive[B[i]] = max(arrive[B[i]], v + ans[i])

print(*ans[1:])
