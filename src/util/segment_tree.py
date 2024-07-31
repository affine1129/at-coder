class SegmentTree:
    # 1-index
    def __init__(self, size: int, init_val: int, func) -> None:
        self.num = (1 << size.bit_length()) - 1
        self.tree = [init_val] * (self.num << 1)
        self.func = func
        self.init_val = init_val

    def update(self, index: int, updated_val: int) -> None:
        tar = index + self.num
        self.tree[tar] = updated_val
        while tar > 0:
            self.tree[tar >> 1] = self.func([self.tree[tar], self.tree[tar ^ 1]])
            tar >>= 1

    def query(self, start: int, end: int) -> int:
        ret = self.init_val
        l, r = start + self.num, end + self.num
        while l < r:
            if l & 1:
                ret = self.func([ret, self.tree[l]])
                l += 1
            if r & 1:
                ret = self.func([ret, self.tree[r - 1]])
            l >>= 1
            r >>= 1

        return ret


if __name__ == '__main__':
    size = 8
    init_val = 0
    func = sum

    seg_tree = SegmentTree(size, init_val, func)
    seg_tree.update(2, 1)
    seg_tree.update(6, 1)
    seg_tree.update(8, 1)
    print(seg_tree.tree)
    print(seg_tree.query(2, 3))
