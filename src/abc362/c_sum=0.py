import sys

input = sys.stdin.readline

N = int(input())

L, R = [0] * N, [0] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())

sum_l = sum(L)
sum_r = sum(R)

if sum_l > 0 or sum_r < 0:
    print('No')
    exit()

sum_ = sum_l
X = []
for l, r in zip(L, R):
    t = min(r - l, -sum_)
    sum_ += t
    X.append(t + l)

print('Yes')
print(*X)
