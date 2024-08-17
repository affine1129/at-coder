from collections import deque

Q = int(input())

deck = deque([])
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        deque.appendleft(deck, x)
    elif t == 2:
        deque.append(deck, x)
    elif t == 3:
        print(deck[x - 1])
