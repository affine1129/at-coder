import sys

input = sys.stdin.readline

N = int(input())
S = input()
Q = int(input())
T_X_C = [tuple(input().split()) for _ in range(Q)]

s_list = [s for s in S[:-1]]
f_idx = 0
for idx, t in enumerate(reversed(T_X_C)):
    if t[0] in {'2', '3'}:
        f_idx = (Q - 1) - idx
        break

count = 0
for t, x, c in T_X_C:
    if t == '1':
        s_list[int(x)-1] = c
    elif count == f_idx:
        if t == '2':
            s_list = list(map(lambda s: s.lower(), s_list))
        elif t == '3':
            s_list = list(map(lambda s: s.upper(), s_list))
    count += 1

print(''.join(s_list))
