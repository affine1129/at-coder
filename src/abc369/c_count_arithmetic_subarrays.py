from collections import Counter

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

pre = A[0]
cur = A[1]
count = 1
counter = Counter()
diff = cur - pre
num = diff
pre = cur
for i in range(1, N - 1):
    cur = A[i + 1]
    diff = cur - pre
    if diff == num:
        count += 1
    else:
        counter[count] += 1
        count = 1
        num = diff
    pre = cur
else:
    counter[count] += 1

ans = N
for count, num in counter.items():
    sum_ = 0
    for i in range(1, count + 1):
        sum_ += i
    ans += sum_ * num

print(ans)
