N = int(input())
A, B, C = map(int, input().split())
MAX = 9999

ans = set()
for i in range(MAX+1):
    for j in range(MAX+1):
        tmp = N - (i*A + j*B)
        if tmp < 0:
            break
        if tmp % C != 0:
            continue

        ans.add(tmp // C + i + j)

print(min(ans))
