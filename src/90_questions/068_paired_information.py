N = int(input())
Q = int(input())


class UnionFind:
    def __init__(self, num):
        self.par = [-1 for _ in range(num)]

    def root(self, x) -> int:
        root = x
        while self.par[root] != -1:
            root = self.par[root]
        while root != x:
            par = self.par[x]
            self.par[x] = root
            x = par
        return x

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        else:
            self.par[root_x] = root_y


queries = [tuple(map(int, input().split())) for _ in range(Q)]

arr = [0] * N
tars = sorted(list(filter(lambda x: x[0] == 0, queries)))
for _, _, Y, V in tars:
    Y -= 1
    arr[Y] = V - arr[Y - 1]


uf = UnionFind(N)
for T, X, Y, V in queries:
    X -= 1
    Y -= 1
    if T == 0:
        uf.unite(X, Y)
    elif T == 1:
        if uf.is_same(X, Y):
            if (X + Y) % 2 == 0:
                diff = arr[Y] + (V - arr[X])
            else:
                diff = arr[Y] - (V - arr[X])
            print(diff)
        else:
            print('Ambiguous')
