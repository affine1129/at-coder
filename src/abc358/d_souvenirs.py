from collections import deque

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

ans = 0
tmp_A = deque(A)
for b in B:
    while len(tmp_A) > 0:
        t = tmp_A[0]
        if b <= t:
            ans += t
            tmp_A.popleft()
            break
        tmp_A.popleft()
    else:
        ans = -1

print(ans)
