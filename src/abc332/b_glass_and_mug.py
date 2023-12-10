K, G, M = map(int, input().split())

cup = 0
mug = 0
for _ in range(K):
    if cup == G:
        cup = 0
    elif mug == 0:
        mug = M
    else:
        diff = min(mug, G-cup)
        cup += diff
        mug -= diff

print(cup, mug)
