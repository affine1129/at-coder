N, M = map(int, input().split())
S = [input() for _ in range(N)]

bits = []
for s in S:
    num = 0
    for i, c in enumerate(s):
        if c == 'o':
            num += 2 ** i
    else:
        bits.append(num)

goal = 2 ** M - 1
ans = 11
for n in range(1, 2 ** N):
    #  max_ = max(solve(n, set(range(N)), bits))
    tmp = n
    sum_ = 0
    count = 0
    num = 0
    while tmp > 0:
        if tmp & 1:
            sum_ |= bits[count]
            num += 1
        tmp = tmp >> 1
        count += 1
    if sum_ == goal:
        ans = min(ans, num)

print(ans)
