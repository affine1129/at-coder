N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    pro_i = A[i]
    for j in range(i + 1, N):
        pro_j = pro_i * A[j] % P
        for k in range(j + 1, N):
            pro_k = pro_j * A[k] % P
            for l in range(k + 1, N):
                pro_l = pro_k * A[l] % P
                for m in range(l + 1, N):
                    pro_m = pro_l * A[m] % P
                    if pro_m == Q:
                        ans += 1
                    pro_m = pro_l
                pro_l = pro_k
            pro_k = pro_j
        pro_j = i

print(ans)
