import heapq

N, M = map(int, input().split())
S = list(input())
T = input()

ma = N - M + 1
used = [False] * ma
regs = list()
q = []
for i in range(M):
    regs += ['#'*i + T[i:j] + '#'*(M-j) for j in range(M, i, -1)]

def check(index, cur):
    if used[index]: 
        return
    res = True
    for m in range(M):
        tar = cur[index+m]
        res &= (tar == '#' or tar == T[m])
    if res:
        used[index] = True
        heapq.heappush(q, index)
    
cur = S 
for i in range(ma):
    check(i, cur)
    
index = N+1
while q:
    index = heapq.heappop(q)
    for i in range(M):
        cur[index+i] = '#'
    for i in range(max(0, index-M+1), min(index+M, ma)):
        check(i, cur)

if ''.join(cur) == '#'*N:
    print('Yes')
else:
    print('No')
