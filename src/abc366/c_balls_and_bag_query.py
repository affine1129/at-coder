from collections import Counter
import sys

input = sys.stdin.readline

Q = int(input())

bag = Counter()
count = 0
for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        if bag[query[1]] == 0:
            count += 1
        bag[query[1]] += 1
    elif query[0] == 2:
        if bag[query[1]] == 1:
            count -= 1
        bag[query[1]] -= 1
    elif query[0] == 3:
        print(count)
