import sys

input = sys.stdin.readline
MIN = -((10 ** 9) * 500) - 1


class SegTree:
    def __init__(self, list_: list[int]) -> None:
        adj = (1 << (len(list_) - 1).bit_length())
        diff = adj - len(list_)
        self.num = adj - 1
        self.tree = [MIN] * self.num + list_ + [MIN] * diff
        for n in range(self.num - 1, 0, -1):
            self.tree[n] = max(self.tree[n << 1], self.tree[n << 1 | 1])

    def update(self, index: int, value: int) -> None:
        index += self.num
        self.tree[index] = value
        while index > 0:
            self.tree[index >> 1] = max(self.tree[index], self.tree[index ^ 1])
            index >>= 1

    def query(self, start: int, end: int) -> int:
        ret = MIN
        start += self.num
        end += self.num
        while start < end:
            if start & 1:
                ret = max(self.tree[start], ret)
                start += 1
            if end & 1:
                ret = max(self.tree[end - 1], ret)
            start >>= 1
            end >>= 1

        return ret


W, N = map(int, input().split())
L, R, V = [], [], []
for _ in range(N):
    l, r, v = map(int, input().split())
    L.append(l)
    R.append(r)
    V.append(v)

pre_tree = SegTree([0] + [MIN] * W)

for i in range(N):
    v = V[i]
    l = L[i]
    r = R[i]
    nex_tree = SegTree([MIN] * (W + 1))
    for j in range(W + 1):
        start = max(j - r, 0)
        end = max(j - l + 1, 0)
        if start == 0 and end == 0:
            nex_val = pre_tree.query(j, j + 1)
        else:
            nex_val = max(pre_tree.query(j, j + 1), pre_tree.query(start, end) + v)
        nex_tree.update(j, nex_val)
    pre_tree = nex_tree

ans = pre_tree.query(W, W + 1)
print(ans) if ans > 0 else print(-1)
