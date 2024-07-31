from collections import deque
from typing import Tuple

import sys

input = sys.stdin.readline


class LazySegmentTree:
    # 1-index
    def __init__(self, size: int, init_val: int, func) -> None:
        self.num = (1 << ((size - 1).bit_length()))
        self.tree = [init_val] * (self.num * 2)
        self.lazy_tree = [0] * (self.num * 2)
        self.func = func
        self.init_val = init_val

    def _get_targets(self, l: int, r: int) -> set[int]:
        tar = set()
        while l < r:
            if l & 1:
                tar.add(l)
                l += 1
            if r & 1:
                tar.add(r - 1)
            l >>= 1
            r >>= 1

        return tar

    def _lazy_update(self, l: int, r: int) -> None:
        q: deque[Tuple[int, int, int]] = deque([(1, self.num, self.num * 2 - 1)])
        while q:
            p1, start, end = q.popleft()
            mid = (start + end) // 2
            n1 = self.lazy_tree[p1]
            self.lazy_tree[p1] = 0

            p2 = p1 << 1
            p3 = (p1 << 1) | 1
            for p, s, e in [(p2, start, mid), (p3, mid + 1, end)]:
                self.tree[p] = n1 or self.tree[p]
                self.lazy_tree[p] = n1 or self.lazy_tree[p]
                if not ((r <= s or e < l) or (l <= s and e < r)):
                    q.append((p, s, e))

    # 0-index
    def update(self, start: int, end: int, updated_val: int) -> None:
        l, r = start + self.num, end + self.num
        tar = self._get_targets(l, r)
        for t in tar:
            self.tree[t] = updated_val
            self.lazy_tree[t] = updated_val
            while t > 0:
                self.tree[t >> 1] = self.func([self.tree[t], self.tree[t ^ 1]])
                t >>= 1

    # 0-index
    def query(self, start: int, end: int) -> int:
        l, r = start + self.num, end + self.num
        tar = self._get_targets(l, r)
        self._lazy_update(l, r)
        ret = self.func([self.tree[t] for t in tar])

        return ret


W, N = map(int, input().split())
ls = LazySegmentTree(W, 1, max)

for _ in range(N):
    L, R = map(int, input().split())
    L -= 1
    ans = ls.query(L, R)
    print(ans)
    ls.update(L, R, ans + 1)
