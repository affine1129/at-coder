import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(lambda x: int(x) + 1, input().split()))

A.sort()
B.sort()
A_B = A + B
A_B.sort()
dp = [M] * (N + M)

next_a = 0
next_b = 0
for i in range(N + M):
    for j in range(next_a, N):
        if A_B[i] >= A[j]:
            dp[i] -= 1
        else:
            next_a = j
            break
    else:
        next_a = N

    for j in range(next_b, M):
        if A_B[i] >= B[j]:
            dp[i] -= 1
        else:
            next_b = j
            break
    else:
        next_b = M

    if dp[i] <= 0:
        print(A_B[i])
        break
    else:
        dp[i+1] = dp[i]
            
