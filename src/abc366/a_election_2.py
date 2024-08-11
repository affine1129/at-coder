N, T, A = map(int, input().split())

rem = N - (T + A)
diff = abs(T - A)

if rem < diff:
    print('Yes')
else:
    print('No')
