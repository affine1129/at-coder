import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline
MOD = 998244353

N = int(input())
P_Q = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N-1)]

inv = [0,1] + [pow(i, -1, MOD) for i in range(2, N+1)]

class UnionFind():
    def __init__(self, n):
        self.cur_idx = n
        MAX_ = n+n-1
        self.par = [-1 for _ in range(MAX_)]
        self.size_ = [1] * MAX_
        self.es = [[] for _ in range(MAX_)]
        self.ans = [0] * N

    def calc_rate(self, x, cur_rate):
        if x < N:
            self.ans[x] = cur_rate
            return
        
        for to, rate in self.es[x]:
            self.calc_rate(to, (cur_rate + rate) % MOD)

    def root(self, x):
        if self.par[x] == -1:
            return x 
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        px = self.root(x)
        py = self.root(y)

        # 親ノードの参照を更新
        self.par[px] = self.cur_idx
        self.par[py] = self.cur_idx

        # 親ノードのサイズを更新
        size_sum = self.size_[px] + self.size_[py]
        self.size_[self.cur_idx] = size_sum 

        # ノード毎のrateを更新
        self.es[self.cur_idx].append([px, inv[size_sum] * self.size_[px] % MOD])    
        self.es[self.cur_idx].append([py, inv[size_sum] * self.size_[py] % MOD])    

        self.cur_idx += 1


uf = UnionFind(N)
for p, q in P_Q:
   uf.unite(p, q) 

uf.calc_rate(N+N-2, 0)

print(*uf.ans)
