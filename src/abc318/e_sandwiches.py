import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


ans = 0
idx_sum = [0] * (N+1)
count = [0] * (N+1)
for i, a in enumerate(A):
    if count[a] > 0:
        ans += i * count[a]
        ans -= count[a]
        ans -= idx_sum[a]
        ans -= count[a] * (count[a] - 1) // 2
    count[a] += 1 
    idx_sum[a] += i

print(int(ans))
