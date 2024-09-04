from typing import Optional

H, W = map(int, input().split())

C = [list(input()) for _ in range(H)]

seen = [False] * (H * W)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

starts = []
for i in range(H):
    for j in range(W):
        count = 0
        if i != 0:
            count += int(C[i - 1][j] == '.')
        if i != (H - 1):
            count += int(C[i + 1][j] == '.')
        if j != 0:
            count += int(C[i][j - 1] == '.')
        if j != (W - 1):
            count += int(C[i][j + 1] == '.')

        if count >= 2 and C[i][j] == '.':
            starts.append((i, j))


def dfs(point: tuple[int, int], dir: Optional[tuple[int, int]], seen: list[bool]) -> int:
    h, w = point
    seen[h * W + w] = True
    ret = -256
    for d in directions:
        if d == dir:
            continue
        if (h + d[0], w + d[1]) == start:
            return 1

        if h != (H - 1) and d == (1, 0) and C[h + 1][w] == '.' and not seen[(h + 1) * W + w]:
            ret = max(ret, dfs((h + 1, w), (-1, 0), seen[:]))
        elif h != 0 and d == (-1, 0) and C[h - 1][w] == '.' and not seen[(h - 1) * W + w]:
            ret = max(ret, dfs((h - 1, w), (1, 0), seen[:]))
        elif w != (W - 1) and d == (0, 1) and C[h][w + 1] == '.' and not seen[h * W + (w + 1)]:
            ret = max(ret, dfs((h, w + 1), (0, -1), seen[:]))
        elif w != 0 and d == (0, -1) and C[h][w - 1] == '.' and not seen[h * W + (w - 1)]:
            ret = max(ret, dfs((h, w - 1), (0, 1), seen[:]))

    return ret + 1


ans = -1
for start in starts:
    ans = max(ans, dfs(start, None, seen))
print(ans if ans > 0 else -1)
