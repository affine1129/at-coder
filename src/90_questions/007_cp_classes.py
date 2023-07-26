import sys
import bisect

input = sys.stdin.readline
INF = 1 << 60

N = int(input())
A_list = sorted((map(int, input().split())))
Q = int(input())
B_list = [int(input()) for _ in range(Q)]

ans = []
for b in B_list:
    idx = bisect.bisect_left(A_list, b)
    if idx != N:
        res1 = abs(A_list[idx] - b)
    else:
        res1 = INF

    if idx != 0:
        res2 = abs(A_list[idx-1] - b)
    else:
        res2 = INF

    ans.append(min([res1, res2]))

print(*ans, sep='\n')
