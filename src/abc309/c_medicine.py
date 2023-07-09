# imos
import sys
from collections import defaultdict

input = sys.stdin.readline

d = defaultdict(int)

N, K = map(int, input().split())
for _ in range(N):
    a, b = map(int, input().split())
    d[1] += b
    d[1+a] -= b

days = sorted(d.keys())

for idx in range(len(days)):
    if d[days[idx]] <= K:
        print(days[idx])
        break
    else:
        d[days[idx+1]] += d[days[idx]]

