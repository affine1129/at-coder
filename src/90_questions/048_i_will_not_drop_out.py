N, K = map(int, input().split())
A_B = [list(map(int, input().split())) for _ in range(N)]

points = []
for a, b in A_B:
    points.append(b)
    points.append(a - b)

points = sorted(points, reverse=True)

print(sum(points[:K]))
