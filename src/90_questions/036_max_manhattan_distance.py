import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
sum_ = []
diff = []
for _ in range(N):
    x, y = map(int, input().split())
    sum_.append(x + y)
    diff.append(x - y)

sum_max = max(sum_)
sum_min = min(sum_)
diff_max = max(diff)
diff_min = min(diff)

for _ in range(Q):
    q = int(input()) - 1
    print(max(sum_[q] - sum_min, diff[q] - diff_min, diff_max - diff[q], sum_max - sum_[q]))
