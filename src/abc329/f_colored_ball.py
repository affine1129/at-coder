import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
C = list(map(lambda x: set({int(x)}), input().split()))

box = C
for _ in range(Q):
    A, B = map(lambda x: int(x)-1, input().split())
    if len(box[A]) < len(box[B]):
        box[B] |= box[A]
    else:
        box[A] |= box[B]
        box[B] = box[A]

    box[A] = set()
    print(len(box[B]))
