import numpy as np

N = int(input())

A = [0]
B = [0]
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


def calc_func(f, g):
    len_ = 1
    while len_ < len(f) + len(g) + 1:
        len_ *= 2

    ff = np.fft.rfft(f, len_)
    fg = np.fft.rfft(g, len_)

    fh = ff * fg

    h = np.fft.irfft(fh, len_)
    h = np.rint(h).astype(np.int64)

    return h


ans = calc_func(A, B)

for a in ans[1:2 * N + 1]:
    print(int(a))
