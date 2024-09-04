N = int(input())
A = list(map(int, input().split()))

sum_ = sum(A)
par = sum_ / 10
AA = A + A

head = 0
tail = 0
cur = 0
while True:
    if cur < par:
        cur += AA[head]
        head += 1
    elif cur > par:
        cur -= AA[tail]
        tail += 1
    else:
        print('Yes')
        exit()
    if head > (N * 2 - 2):
        break

print('No')
