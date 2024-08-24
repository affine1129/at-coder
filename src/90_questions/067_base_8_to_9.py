N, K = map(int, input().split())

base8 = list(map(int, list(str(N))[::-1]))
for _ in range(K):
    base10 = sum(base8[i] * (8 ** i) for i in range(len(base8)))
    base8 = []
    while base10 > 0:
        mod = base10 % 9
        base8.append(5 if mod == 8 else mod)
        base10 //= 9

print(''.join(map(str, base8[::-1])) or 0)
