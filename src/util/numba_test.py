import time
from numba import jit
import numpy as np

# 通常のPython関数


def sum_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Numbaを使った関数


@jit(nopython=True)
def sum_array_numba(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


# データの準備
arr = np.arange(10 ** 7)

# 実行時間の測定

start = time.time()
print(sum_array(arr))
print("通常の関数の実行時間:", time.time() - start)

start = time.time()
print(sum_array_numba(arr))
print("Numba関数の実行時間:", time.time() - start)
