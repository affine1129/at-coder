import sys
from collections import deque

input = sys.stdin.readline

N1, N2, M = map(int, input().split())
N = N1 + N2

a_b_list = [list(map(int, input().split())) for _ in range(M)]
queue = deque()
depth_list = [0] * N
d_list = [[] for _ in range(N)]

for a_b in a_b_list:
    d_list[a_b[0]-1].append(a_b[1])
    d_list[a_b[1]-1].append(a_b[0])

def bfs(num):
    queue.append(num)
    depth_list[num-1] = 1
    while len(queue) != 0:
        num = queue.popleft()
        for d in d_list[num-1]:
            if depth_list[d-1] == 0:
                depth_list[d-1] = depth_list[num-1] + 1
                queue.append(d)
bfs(1)
bfs(N)

result = max(depth_list[:N1]) + max(depth_list[N1:]) - 1
print(result)
