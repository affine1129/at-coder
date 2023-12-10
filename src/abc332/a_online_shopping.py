import sys

input = sys.stdin.readline

N, S, K = map(int, input().split())

sum = 0
for _ in range(N):
    P, Q = map(int, input().split())
    sum += P * Q
else:
    if sum < S:
        sum += K

print(sum)
