N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = 10 ** 10
for k in range(K + 1):
    ans = min(ans, A[N - (K - k) - 1] - A[k])

print(ans)
