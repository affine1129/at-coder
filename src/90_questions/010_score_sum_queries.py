import sys

input = sys.stdin.readline

N = int(input())
p = [[0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    C, P = map(int, input().split())
    if C == 1:
        p[i][0] += p[i-1][0] + P
        p[i][1] += p[i-1][1]
    else:
        p[i][0] += p[i-1][0]
        p[i][1] += p[i-1][1] + P
    
Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    print(p[r][0]-p[l-1][0], p[r][1]-p[l-1][1])
             
