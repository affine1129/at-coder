S = list(input())
T = list(input())

ans = []
tmp = S
for i in range(len(S)):
    if S[i] > T[i]:
        tmp[i] = T[i]
        ans.append(''.join(tmp))

for i in range(-1, -(len(S) + 1), -1):
    if S[i] < T[i]:
        tmp[i] = T[i]
        ans.append(''.join(tmp))

print(len(ans))
if ans:
    print('\n'.join(ans))
