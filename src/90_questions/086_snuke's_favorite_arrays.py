N, Q = map(int, input().split())

MOD = 10 ** 9 + 7

xyzw = [list(map(int, input().split())) for _ in range(Q)]


def check(index: int, bit: int) -> bool:
    for x, y, z, w in xyzw:
        if (bit >> (x - 1) & 1) | (bit >> (y - 1) & 1) | (bit >> (z - 1) & 1) != (w >> index & 1):
            break
    else:
        return True

    return False


ans = 1
for i in range(60):
    sum_ = 0
    for j in range(2 ** N):
        sum_ += int(check(i, j))
    ans *= sum_
    ans %= MOD

print(ans)
