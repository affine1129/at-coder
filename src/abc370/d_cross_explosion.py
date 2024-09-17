import bisect
from typing import Optional
# https://qiita.com/Shirotsume/items/706742162db68c481c3c
from sortedcontainers import SortedSet

H, W, Q = map(int, input().split())

hls = [SortedSet(range(H)) for _ in range(W)]
wls = [SortedSet(range(W)) for _ in range(H)]


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

    return i1 is not None or i2 is not None


for _ in range(Q):
    R, C = map(int, input().split())
    R, C = R - 1, C - 1

    if initial_remove(R, C):
        continue

    index = bisect.bisect_left(wls[R], C)
    if index != len(wls[R]):
        tmp = wls[R].pop(index)
        hls[tmp].discard(R)
    if index != 0:
        tmp = wls[R].pop(index - 1)
        hls[tmp].discard(R)

    index = bisect.bisect_left(hls[C], R)
    if index != len(hls[C]):
        tmp = hls[C].pop(index)
        wls[tmp].discard(C)
    if index != 0:
        tmp = hls[C].pop(index - 1)
        wls[tmp].discard(C)


print(sum([len(wls[i]) for i in range(H)]))
