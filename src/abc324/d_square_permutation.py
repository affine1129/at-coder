N = int(input())
S = int(''.join(sorted(input())))

count = 0
ans = 0
while count**2 < 10**N:
    num = int(''.join(sorted(str(count ** 2))))
    if num == S:
        ans += 1
    count += 1

print(ans)
