import copy

H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]


comb = 2 ** H

ans = [0] * comb
for i in range(comb):
    tar = i
    check = []
    index = 0
    count = 0
    while tar > 0:
        if tar & 1:
            if check == []:
                check = copy.copy(grid[index])
            else:
                for w in range(W):
                    check[w] = check[w] if check[w] == grid[index][w] else -1
            count += 1
        tar >>= 1
        index += 1

    if count == 0:
        continue
    else:
        set_ = set(check) - {-1}
        for s in set_:
            ans[i] = max(ans[i], len(list(filter(lambda x: x == s, check))) * count)


print(max(ans + [1]))
