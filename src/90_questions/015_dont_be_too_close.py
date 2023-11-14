MOD = 10 ** 9 + 7
N = int(input())

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

# fact[n] = (n! mod p)
fact = [1] * N
# factinv[n] = ((n!)^(-1) mod p)
factinv = [1] * N
# factinv 計算用
inv = [1] * N 
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

for k in range(1, N+1):
    count = 0
    for i in range(1, N+1):
        if i == 1:
            n = N
        else:
            n = N - ((i-1) * (k-1))
            if n < i:
                continue
        r = i 

        count += cmb(n, r, MOD)
        count %= MOD
    print(count)

