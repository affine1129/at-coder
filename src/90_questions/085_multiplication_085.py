import math

K = int(input())

ans = 0
for i in range(1, int(math.sqrt(K)) + 1):
    if K % i != 0:
        continue
    k = K // i
    for j in range(i, int(math.sqrt(k)) + 1):
        if k % j == 0:
            ans += 1

print(ans)
