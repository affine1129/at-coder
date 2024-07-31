from collections import Counter, deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
q = deque([])
counter = Counter()
num = 0
left = 0
ans = 0
for right in range(N):
    right_val = A[right]
    q.append(right_val)
    if counter[right_val] == 0:
        num += 1
    counter[right_val] += 1

    if num > K:
        ans = max(ans, right - left)
        while num > K:
            left += 1
            left_val = q.popleft()
            counter[left_val] -= 1
            if counter[left_val] == 0:
                num -= 1
else:
    ans = max(ans, N - left)

print(ans)
