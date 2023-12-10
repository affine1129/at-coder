N, M = map(int, input().split())
S = input()

count = 0
rem_t = M
rem_l = 0
for s in S:
    if s == '0':
        rem_t = M
        rem_l = count

    if s == '1':
        if rem_t > 0:
            rem_t -= 1
        elif rem_l > 0:
            rem_l -= 1
        else:
            count += 1

    if s == '2':
        if rem_l > 0:
            rem_l -= 1
        else:
            count += 1

print(count)
