class UnionFind():
    def __init__(self, n):
       self.par = [i for i in range(n+1)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x] 

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.par[x] = y

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
P_A_B = [list(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(N)
for p, a, b in P_A_B:
    if p == 0:
        uf.unite(a, b)
    if p == 1:
        if uf.is_same(a, b):
            print('Yes')
        else:
            print('No')
