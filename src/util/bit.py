# 参考：http://hos.ac/slides/20140319_bit.pdf

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
        return self.sum(right) - self.sum(left)
