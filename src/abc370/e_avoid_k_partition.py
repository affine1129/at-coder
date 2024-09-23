from collections import defaultdict

MOD = 998244353

N, K = map(int, input().split())
A = map(int, input().split())

m = defaultdict(int)

dp = all = m[0] = 1
acc = 0
for a in A:
    acc += a
    dp = (all - m[acc - K]) % MOD
    all += dp
    m[acc] += dp

print(dp)
