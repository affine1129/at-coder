N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

ans = 0
index = 0
tmp = 0
for b in B:
    for a in A[index:]:
        if a >= b:
            ans += a
            index = tmp + 1
            break
        else:
            tmp += 1
            continue
    else:
        ans = -1
        break

print(ans)
