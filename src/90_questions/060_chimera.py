import bisect

N = int(input())
A = list(map(int, input().split()))

MAX = 10 ** 9


def lis(list_: list) -> list:
    len_ = len(list_)
    dp = [MAX] * len_
    ret = [0] * len_
    for i in range(len_):
        tar = list_[i]
        index = bisect.bisect_left(dp, tar)
        if tar < dp[index]:
            dp[index] = tar
        ret[i] = index + 1

    return ret


lis1 = lis(A)
lis2 = lis(A[::-1])[::-1]

ans = 0
for i in range(N):
    ans = max(ans, lis1[i] + lis2[i] - 1)

print(ans)
