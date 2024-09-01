N = int(input())

L, R = [], []
for _ in range(N):
    A, S = input().split()
    if S == 'L':
        L.append(int(A))
    else:
        R.append(int(A))

ans = 0
if L != []:
    l = L[0]
    for i in range(1, len(L)):
        ans += abs(l - L[i])
        l = L[i]

if R != []:
    r = R[0]
    for i in range(1, len(R)):
        ans += abs(r - R[i])
        r = R[i]

print(ans)
