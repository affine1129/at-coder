N = int(input())
S = input()

pre = S[0]
count = 1
di = {}
for c in S[1:]:
    if pre == c:
        count += 1
    else:
        di[pre] = max(di.get(pre, 0), count)
        count = 1
    pre = c
else:
    di[pre] = max(di.get(pre, 0), count)

ans = sum(di.values())
print(ans)
