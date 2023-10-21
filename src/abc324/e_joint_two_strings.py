import sys

input = sys.stdin.readline

N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

tl = len(T)
rt = T[::-1]
fl = [0] * len(S)
bl = [0] * (tl+1)

def calc(s, t):
    count = 0
    for c in s:
        if count == tl:
            return count
        if c == t[count]:
            count += 1
    return count

for i, s in enumerate(S):
    fl[i] = calc(s, T)

    bl[calc(s[::-1], rt)] += 1

ans = 0 
for f in fl:
    ans += sum(bl[tl-f:])
print(ans)
