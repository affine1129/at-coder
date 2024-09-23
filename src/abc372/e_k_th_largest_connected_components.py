N, Q = map(int, input().split())


class UnionFind():
    def __init__(self, num: int) -> None:
        self.parents = [i for i in range(num)]
        self.ls = [[i] for i in range(num)]

    def root(self, a: int) -> int:
        cur = a
        while self.parents[cur] != cur:
            cur = self.parents[cur]
        self.parents[a] = cur
        return cur

    def union(self, a: int, b: int) -> None:
        ra = self.root(a)
        rb = self.root(b)
        if ra != rb:
            self.parents[rb] = ra
            self.ls[ra] += self.ls[rb]
            self.ls[ra] = sorted(self.ls[ra], reverse=True)[:10]
            self.ls[rb] = []


uf = UnionFind(N)
for _ in range(Q):
    a, b, c = map(int, input().split())
    b, c = b - 1, c - 1

    if a == 1:
        uf.union(b, c)

    if a == 2:
        ls = uf.ls[uf.root(b)]
        print(-1 if len(ls) <= c else ls[c] + 1)
