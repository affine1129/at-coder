
K = int(input())
C = list(map(int, input().split()))

dp = [0] * (K + 1)

MOD = 998244353
N = 10 ** 6

# fact[n] = (n! mod p)
fact = [1, 1]
# factinv[n] = ((n!)^(-1) mod p)
factinv = [1, 1]
# factinv 計算用
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

dp[0] = 1
for i in range(len(C)):
    for j in range(K, -1, -1):
        for k in range(min(C[i], K - j) + 1):
            if k == 0:
                continue
            dp[j + k] += dp[j] * factinv[k] % MOD
            dp[j + k] %= MOD

print((sum([d * fact[i] % MOD for i, d in enumerate(dp)]) - 1) % MOD)
