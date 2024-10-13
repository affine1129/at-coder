import math

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
point = (0, 0)
for i in range(N):
    X, Y = XY[i]
    ans += math.sqrt((point[0] - X) ** 2 + (point[1] - Y) ** 2)
    point = X, Y
else:
    ans += math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)

print(ans)
