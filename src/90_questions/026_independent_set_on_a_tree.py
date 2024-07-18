import sys
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

tree = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].add(B)
    tree[B].add(A)

ans1, ans2 = set(), set()
q = deque([1])
nex_q: deque[int] = deque([])
count = 0
seen = [False] * (N + 1)
while q or nex_q:
    if not q:
        q = nex_q
        nex_q = deque([])
        count += 1

    tar = q.pop()
    seen[tar] = True
    for t in tree[tar]:
        if seen[t]:
            continue
        nex_q.append(t)

    if count % 2 == 0:
        ans1.add(tar)
    else:
        ans2.add(tar)

if len(ans1) < len(ans2):
    print(*list(ans2)[:N // 2])
else:
    print(*list(ans1)[:N // 2])
