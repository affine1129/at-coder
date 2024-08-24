N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_ = sum(A)
A += A

ans = 0
d = 0
mod_ls = [0] * M
for i in range(N * 2):
    if i >= N:
        mod_ls[(d - sum_) % M] -= 1
        ans += mod_ls[d % M]
    mod_ls[d % M] += 1
    d += A[i]

print(ans)
