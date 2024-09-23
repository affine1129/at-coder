import math

M = int(input())

num = M
ans = []
while num >= 3:
    tmp = int(math.log(num, 3))
    ans.append(tmp)
    num -= 3 ** tmp

for _ in range(num):
    ans.append(0)

print(len(ans))
print(*ans)
