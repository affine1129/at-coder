N, X, Y = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)

ans = 0
sum_a = 0
sum_b = 0
for i in range(N):
    sum_a += A[i]
    sum_b += B[i]
    if sum_a > X or sum_b > Y:
        ans = i + 1
        break
else:
    ans = N

print(ans)
