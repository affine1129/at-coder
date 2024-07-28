import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
for _ in range(Q):
    b, k = map(int, input().split())
    l, h = -1, 10 ** 9
    while l + 1 < h:
        m = (l + h) // 2
        c = bisect_right(A, b + m) - bisect_left(A, b - m)
        if c >= k:
            h = m
        else:
            l = m
    else:
        print(h)
