MOD = 998244353

K = int(input())
C = list(map(int, input().split()))

C_len = len(C)
C1_len = C_len + 1

dp = [[0] * (K + 1) for _ in range(C1_len)]


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


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

dp[0][0] = 1
for i in range(C_len):
    for j in range(K + 1):
        for k in range(C[i] + 1):
            if k == 0:
                dp[i + 1][j] += dp[i][j]
            elif j + k <= K:
                dp[i + 1][j + k] += dp[i][j] * cmb(K - j, k, MOD)
            else:
                break

print(dp)
print(sum(dp[-1]) - 1)
