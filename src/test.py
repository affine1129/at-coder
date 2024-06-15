import time
import numpy as np

def numpy_test():
    list_ = np.array([0] * (10 ** 5))

    for i in range(10 ** 5):
        list_[i] += 1

def set_union_test():
    set_a = {1}
    set_b = set([i for i in range(10**5)])
    for _ in range(10**3):
        set_b |= set_a
        set_a = set_b
    set_b = set()

def main():
    # 時間計測開始
    time_sta = time.time()

    # 処理を書く
    #  numpy_test()
    set_union_test()

    # 時間計測終了
    time_end = time.time()
    # 経過時間（秒）
    tim = time_end - time_sta

    print(tim)

if __name__ == '__main__':
    main()
