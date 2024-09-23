from collections import deque

N = int(input())
H = list(map(int, input().split()))

buildings = deque()
ans = []
for h in H[::-1]:
    ans.append(len(buildings))
    while buildings and buildings[-1] < h:
        buildings.pop()
    buildings.append(h)

print(*ans[::-1])
