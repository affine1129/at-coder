N, K = map(int, input().split())
MOD = 10 ** 9 + 7


def f(x: int) -> int:
    ret = 1
    if x == 0:
        ret = 1
    elif x % 2 == 0:
        ret = f(x // 2)
        ret *= ret
        ret %= MOD
    else:
        ret = f(x - 1)
        ret *= (K - 2)
        ret %= MOD
    return ret


ans = 1
if N >= 1:
    ans *= K
    ans %= MOD
if N >= 2:
    ans *= (K - 1)
    ans %= MOD
if N >= 3:
    ans *= f(N - 2)
    ans %= MOD

print(ans)
