import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = input()
C_list = list(map(int, input().split()))

indices = [list() for _ in range(M)]
for idx, c in enumerate(C_list):
    indices[c-1].append(idx)  

ans = [''] * N
for i1, idx_list in enumerate(indices):
    for i2, idx in enumerate(idx_list):
       ans[idx] = S[idx_list[i2-1]]

print(''.join(ans))
