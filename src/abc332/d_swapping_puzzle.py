import sys

input = sys.stdin.readline

H, W = map(int, input().split())

aw = [[] for _ in range(W)]
ah = [[] for _ in range(H)]
for i in range(H):
    A = list(map(int, input().split()))
    ah[i] = sorted(A)
    for i, a in enumerate(A):
       aw[i].append(a) 
else:
    aw = list(map(lambda x: sorted(x), aw))

bw = [[] for _ in range(W)]
bh = [[] for _ in range(H)]
for i in range(H):
    B = list(map(int, input().split()))
    bh[i] = sorted(B)
    for i, b in enumerate(B):
       bw[i].append(b) 
else:
    bw = list(map(lambda x: sorted(x), bw))

count = 0
for a in aw:
    if a in bw:
        i = bw.index(a)
    else:
        print(-1)
        exit()
    count += i
    bw.pop(i)

for a in ah:
    if a in bh:
        i = bh.index(a)
    else:
        print(-1)
        exit()
    count += i
    bh.pop(i)

print(count)

