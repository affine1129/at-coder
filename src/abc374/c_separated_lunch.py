N = int(input())
K = list(map(int, input().split()))

ans = 10 ** 10
for i in range(2**N):
    sum_a = 0
    sum_b = 0
    for j in range(N):
        if (i >> j) & 1:
            sum_a += K[j]
        else:
            sum_b += K[j]
    ans = min(ans, max(sum_a, sum_b))
print(ans)
