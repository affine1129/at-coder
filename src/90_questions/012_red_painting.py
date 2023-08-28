import sys

input = sys.stdin.readline

H, W = map(int, input().split())
Q = int(input())

class UF:
    def __init__(self, h, w):
        self.h = h+2
        self.w = w+2
        # 親ノードの時は負の値でサイズを持つ
        self.par_or_size = [ 0 for _ in range(self.h*self.w)]
    
    def root(self, x):
        p = x
        while self.par_or_size[p] > 0:
            p = self.par_or_size[p]
        while self.par_or_size[x] > 0:
            tmp = self.par_or_size[x]
            self.par_or_size[x] = p
            x = tmp
        return p

    def size(self, x):
        return -self.par_or_size[self.root(x)]

    def unite(self, x):
        self.par_or_size[x] = -1
        for dir in [x-1, x+1, x+self.w, x-self.w]:
            if self.par_or_size[dir] != 0:
                x = self.root(x)
                y = self.root(dir)
                if x == y:
                    return
                if self.size(x) < self.size(y):
                    x, y = y, x
                self.par_or_size[x] += self.par_or_size[y]
                self.par_or_size[y] = x

    def is_same(self, x, y):
        if self.root(x) == self.root(y) and self.par_or_size[x] != 0 and self.par_or_size[y] != 0:
            return True
        else:
            return False


uf = UF(H, W)
for _ in range(Q):
    t_r_c = list(map(int, input().split()))
    if t_r_c[0] == 1:
        r, c = t_r_c[1:]
        uf.unite(r*uf.w+c) 

    else:
        ra, ca, rb, cb = t_r_c[1:]
        ans = uf.is_same(ra*uf.w+ca, rb*uf.w+cb)

        if ans:
            print('Yes')
        else:
            print('No')

