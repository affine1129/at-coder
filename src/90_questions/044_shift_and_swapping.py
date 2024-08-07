import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
A = deque(map(int, input().split()))

for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        x -= 1
        y -= 1
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp
    elif T == 2:
        tmp = A.pop()
        A.appendleft(tmp)
    elif T == 3:
        x -= 1
        print(A[x])
