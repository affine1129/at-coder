import sys

input = sys.stdin.readline

N, D = map(int, input().split())
S_list = [input() for _ in range(N)]

ok = 0
ok_list = []

for d in range(D):
    for s in S_list:
        if s[d] == 'x':
            ok_list.append(ok)
            ok = 0
            break
    else:
        ok += 1
else:
    ok_list.append(ok)

print(max(ok_list))

