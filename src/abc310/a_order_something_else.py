import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())

D_list = list(map(int, input().split()))

D_min = min(D_list)

if (P - Q) < D_min:
    print(P)
else:
    print(Q + D_min)

