import math

A, B, C = map(int, input().split())

g = math.gcd(A, B, C)

ans = 0
if g == 1:
    ans = A + B + C - 3
else:
    ans += A / g - 1
    ans += B / g - 1
    ans += C / g - 1

print(int(ans))
