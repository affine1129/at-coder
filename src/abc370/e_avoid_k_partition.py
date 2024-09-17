MOD = 998244353

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
for _ in range(N - 1):
    ans *= 2
    ans %= MOD

print(ans)

head = 0
tail = 0

sum_ = A[0]
exc = 0
while head != (N - 1) or tail != (N - 1):
    if sum_ <= K and head != (N - 1):
        head += 1
        sum_ += A[head]
    elif sum_ >= K:
        sum_ -= A[tail]
        tail += 1

    exc += bool(sum_ == K)
    exc %= MOD
    print(head, tail)

print(ans - exc + (MOD if ans < exc else 0))
