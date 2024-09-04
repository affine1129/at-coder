L, R = map(int, input().split())

MOD = 10 ** 9 + 7

ans = 0
for i in range(19):
    head = 10 ** i
    tail = head * 10 - 1
    if tail < L:
        continue
    elif R < head:
        break
    else:
        l = max(head, L)
        r = min(tail, R)
        sum_ = (((r + 1) * r // 2) - (l * (l - 1)) // 2) % MOD

        ans += sum_ * (i + 1)
        ans %= MOD


print(ans)
