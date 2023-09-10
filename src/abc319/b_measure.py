N = int(input())

ans = '1'
for i in range(1,N+1):
    for j in range(1,10):
        if i % (N / j) == 0:
            ans += str(j)
            break
    else:
        ans += '-'

print(ans)
