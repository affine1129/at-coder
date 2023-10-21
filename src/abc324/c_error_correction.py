N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

def check(s, t):
    count = 0
    for a, b in zip(t, s):
        if a == b:
            count += 1
        else:
            break
    for a, b in zip(reversed(t), reversed(s)):
        if a == b:
            count += 1
        else:
            break
    return count

ans = []
l = len(T)
for idx, s in enumerate(S):
    if l == len(s):
        count = check(s, T)
        if count >= l-1:
            ans.append(idx+1)

    elif l-1 == len(s):
        count = check(s, T)
        if count >= l-1:
            ans.append(idx+1)

    elif l+1 == len(s):
        count = check(s, T)
        if count >= l:
            ans.append(idx+1)


print(len(ans))
print(*ans)
