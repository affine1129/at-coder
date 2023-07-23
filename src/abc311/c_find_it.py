import sys

input = sys.stdin.readline

N = int(input())
A_list = list(map(lambda x: int(x) - 1, input().split()))

list_ = list()
set_ = set()
tar = 0

while True:
    # 探索済みの場合
    if tar in set_:
        loc = list_.index(tar)
        res_list = list_[loc:]
        print(len(res_list))
        print(' '.join(map(lambda x: str(x + 1), res_list)))
        break
    set_.add(tar)
    list_.append(tar)
    tar = A_list[tar]

