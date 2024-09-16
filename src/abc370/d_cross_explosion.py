import bisect
from typing import Optional
from sortedcontainers import SortedSet, SortedList, SortedDict

H, W, Q = map(int, input().split())

hls = [[i for i in range(H)] for _ in range(W)]
wls = [[i for i in range(W)] for _ in range(H)]


def search(v: int, ls: list[int]) -> Optional[int]:
    head = 0
    tail = len(ls)
    if tail == 0:
        return None
    while head + 1 < tail:
        mid = (head + tail) // 2
        if ls[mid] <= v:
            head = mid
        else:
            tail = mid
    if ls[head] == v:
        return head
    else:
        return None


def initial_remove(h, w) -> bool:
    i1 = search(h, hls[w])
    if i1 is not None:
        del hls[w][i1]
    i2 = search(w, wls[h])
    if i2 is not None:
        del wls[h][i2]

    return bool(i1) or bool(i2)


for _ in range(Q):
    R, C = map(int, input().split())
    R, C = R - 1, C - 1

    if initial_remove(R, C):
        continue

    print('1')
    print(hls)
    print(wls)

    index = bisect.bisect_left(wls[R], C)
    if index != len(wls[R]):
        tmp = wls[R][index]
        del wls[R][index]
        print(index, tmp, R)
        del hls[tmp][R]
    if index != 0:
        tmp = wls[R][index - 1]
        del wls[R][index - 1]
        del hls[tmp][R]

    print('2')
    print(hls)
    print(wls)

    index = bisect.bisect_left(hls[C], R)
    if index != len(hls[C]):
        tmp = hls[C][index]
        del hls[C][index]
        del wls[tmp][C]
    if index != 0:
        tmp = hls[C][index - 1]
        del hls[C][index - 1]
        del wls[tmp][C]

    print('3')
    print(hls)
    print(wls)

print(sum([len(wls[i]) for i in range(H)]))
