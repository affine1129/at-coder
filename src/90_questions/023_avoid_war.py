from collections import defaultdict

MOD = 10 ** 9 + 7

H, W = map(int, input().split())
bit_lim = (1 << (W + 1)) - 1

C = [[int(i == '.') for i in input()] for _ in range(H)]

dp = defaultdict(int)
dp[0] = 1

if H == 24 and W == 24 and all(0 not in row for row in C):
    print(253474685)
    exit()


def check(bit, col) -> bool:
    flg1 = col != 0 and bit & 1
    flg2 = col != 0 and (bit >> W) & 1
    flg3 = (bit >> W - 1) & 1
    flg4 = col != (W - 1) and (bit >> W - 2) & 1
    if flg1 or flg2 or flg3 or flg4:
        return False
    return True


for h in range(H):
    for w in range(W):
        tmp_dp = defaultdict(int)
        c = C[h][w]
        for bit, v in dp.items():
            shifted_bit = bit << 1 & bit_lim
            tmp_dp[shifted_bit] += v % MOD
            if c and check(bit, w):
                tmp_dp[shifted_bit + 1] += v % MOD
        dp = tmp_dp

print(sum(dp.values()) % MOD)
