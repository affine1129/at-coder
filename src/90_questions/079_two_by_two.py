H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        diff = B[i][j] - A[i][j]
        ans += abs(diff)
        A[i][j + 1] += diff
        A[i + 1][j] += diff
        A[i + 1][j + 1] += diff
    else:
        if A[i][W - 1] != B[i][W - 1]:
            print('No')
            break
else:
    if A[H - 1] == B[H - 1]:
        print('Yes')
        print(ans)
    else:
        print('No')
