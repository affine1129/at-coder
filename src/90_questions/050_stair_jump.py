N, L = map(int, input().split())

MOD = 10 ** 9 + 7


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


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

count = N // L

ans = 0
for i in range(count + 1):
    sum_ = (N - i * L) + i
    ans += cmb(sum_, i, MOD)
    ans %= MOD

print(ans)
