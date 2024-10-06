import math
import itertools

N, S, T = map(int, input().split())
ABCD = [tuple(map(int, input().split())) for _ in range(N)]


def cal_len(a, b, c, d):
    return math.sqrt((a - c)**2 + (b - d)**2)


MAX = 10**10
ans = MAX
for per in itertools.permutations(range(N)):
    # 0: AB, 1: CD
    dp: list[list[float]] = [[MAX] * 2 for _ in range(N + 1)]
    dp[0][0] = dp[0][1] = 0
    pos_ab = (0, 0)
    pos_cd = (0, 0)
    for i, p in enumerate(per):
        a, b, c, d = ABCD[p]
        tmp = cal_len(a, b, c, d) / T
        # (A, B)から線を引く
        dp[i + 1][1] = min(
            cal_len(pos_ab[0], pos_ab[1], a, b) / S + tmp + dp[i][0],
            cal_len(pos_cd[0], pos_cd[1], a, b) / S + tmp + dp[i][1],
        )
        # (C, D)から線を引く
        dp[i + 1][0] = min(
            cal_len(pos_ab[0], pos_ab[1], c, d) / S + tmp + dp[i][0],
            cal_len(pos_cd[0], pos_cd[1], c, d) / S + tmp + dp[i][1],
        )
        pos_ab = (a, b)
        pos_cd = (c, d)
    ans = min(ans, *dp[-1])
print(ans)
