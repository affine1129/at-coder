import sys
import numpy as np
 
readline = sys.stdin.buffer.readline

N = int(readline())
X_Y_list = np.array([list(map(int, readline().split())) for _ in range(N)])
X = X_Y_list[:, 0]
Y = X_Y_list[:, 1]

max_ = 0
for i in range(N):
    # X, Yそれぞれの辺のarrayを求める
    _X = np.delete(X, i) - X[i]
    _Y = np.delete(Y, i) - Y[i]
    rad_list1 = np.arctan2(_Y, _X)
    rad_list1.sort()
    rad_list1 = np.concatenate((rad_list1, rad_list1 + 2 * np.pi))

    rad_list2 = rad_list1[:N-1] + np.pi

    rad_list_l = rad_list1[np.searchsorted(rad_list1, rad_list2) - 1]
    rad_diff = rad_list_l - rad_list1[:N-1]
    max_ = max(*rad_diff, max_)

    rad_list_r = rad_list1[np.searchsorted(rad_list1, rad_list2)]
    rad_diff = 2 * np.pi - (rad_list_r - rad_list1[:N-1])
    max_ = max(*rad_diff, max_)

print(max_ / np.pi * 180)

