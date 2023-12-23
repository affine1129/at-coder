import sys
import itertools

input = sys.stdin.readline

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]


def is_same(h, r):
    for hi, i in enumerate(h):
        for rj, j in enumerate(r):
            if A[i][j] != B[hi][rj]:
                return False
    return True


def search():
    count = 0
    for i in itertools.permutations(range(H), H):
        for j in itertools.permutations(range(W), W):
            if is_same(i, j):
                list_ = list(i)
                for k in range(H):
                    index = list_.index(k)
                    count += index
                    list_.pop(index)
                list_ = list(j)
                for k in range(W):
                    index = list_.index(k)
                    count += index
                    list_.pop(index)
                return count
    return -1


print(search())
