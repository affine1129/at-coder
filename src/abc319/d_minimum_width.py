import sys

input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))

left, right = max(L), sum(L) + N - 1
while left < right :
    mid = (right + left) // 2
    length = 0
    count = 1
    for l in L:
        if l <= mid:
            if length + l <= mid:
                length += l + 1
            else:
                length = l + 1
                count += 1
        else:
            count = M + 1
            break

    if count > M:
        left = mid + 1
    else:
        right = mid

print(right)
