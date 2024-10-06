N, X = map(int, input().split())
APBQ = [tuple(map(int, input().split())) for _ in range(N)]


def calc_cost(a, p, b, q, w) -> int:
    min_ = 10 ** 9 + 1
    for i in range(b):
        num_a = i
        num_b = (max(w - num_a * a, 0) + b - 1) // b
        min_ = min(min_, num_a * p + num_b * q)
    return min_


for i in range(N):
    a, p, b, q = APBQ[i]
    if b * p < a * q:
        APBQ[i] = b, q, a, p


head = 0
tail = 10 ** 9 + 1
while head + 1 < tail:
    mid = (head + tail) // 2
    rem_x = X
    for i in range(N):
        a, p, b, q = APBQ[i]

        rem_x -= calc_cost(a, p, b, q, mid)

        if rem_x < 0:
            tail = mid
            break
    else:
        head = mid
print(head)
