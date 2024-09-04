import math

N = int(input())

count = 1
cur = 2
while cur <= math.sqrt(N):
    if N % cur == 0:
        count += 1
        N /= cur
    else:
        cur += 1

ans = (count - 1).bit_length()

print(ans)
