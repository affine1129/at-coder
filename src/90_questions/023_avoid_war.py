import sys

input = sys.stdin.readline

H, W = map(int, input().split())

C = 0
for h in range(H):
    #  C += input().removesuffix('\n')
    for i, c in enumerate(input().removesuffix('\n')):
        C |= 2**(i + h * H) if c == '.' else 0

print(C)
print(bin(C))

list_ = []
for h in range(H):
    for w in range(W - 1):
        tmp = 2**(w + h * H) | 2**((w + 1) + h * H)
        if (tmp & C) == tmp:
            list_.append(tmp)
for w in range(W):
    for h in range(H - 1):
        tmp = 2**(w + h * H) | 2**(w + (h + 1) * H)
        if (tmp & C) == tmp:
            list_.append(tmp)

print(list_)
print(list(map(bin, list_)))

ans = 0
for i in range(2**(H * W)):
    if (i & C) != i:
        continue
    for ls in list_:
        if (i & ls) == ls:
            break
    else:
        ans += 1

print(ans)
