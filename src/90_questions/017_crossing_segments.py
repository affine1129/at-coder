import sys


class BIT:
    def __init__(self, num: int) -> None:
        self.list_ = [0] * (num + 1)

    def add(self, index, value) -> None:
        while index < len(self.list_):
            self.list_[index] += value
            index += index & -index

    def sum(self, index: int) -> int:
        sum = 0
        while index > 0:
            sum += self.list_[index]
            index -= index & -index
        return sum

    def interval_sum(self, left: int, right: int) -> int:
        return self.sum(right) - self.sum(left - 1)


input = sys.stdin.readline

N, M = map(int, input().split())

list_ = [[] for _ in range(N + 1)]
bit = BIT(N + 1)

for _ in range(M):
    l, r = map(int, input().split())
    list_[l].append(r)

ans = 0
for l in range(1, N + 1):
    for r in list_[l]:
        if l + 1 <= r - 1:
            ans += bit.interval_sum(l + 1, r - 1)
    for r in list_[l]:
        bit.add(r, 1)

print(ans)
