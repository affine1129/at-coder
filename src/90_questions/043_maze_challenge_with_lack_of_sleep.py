from collections import deque

H, W = map(int, input().split())
rs, cs = map(lambda x: int(x) - 1, input().split())
rt, ct = map(lambda x: int(x) - 1, input().split())

S = [input() for _ in range(H)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
costs = [[-1] * W for _ in range(H)]


def bfs() -> int:
    q: deque = deque([(0, (rs, cs), (rd, cd)) for rd, cd in directions])
    while q:
        cost, (rp, cp), (rd, cd) = q.popleft()
        while True:
            rp += rd
            cp += cd

            if not (0 <= rp < H and 0 <= cp < W) or S[rp][cp] == '#':
                break

            if costs[rp][cp] == cost:
                continue

            if 0 <= costs[rp][cp] <= cost - 1:
                break

            if rp == rt and cp == ct:
                return cost

            costs[rp][cp] = cost
            for dy, dx in directions:
                if dy == rd and dx == cd:
                    continue
                q.append((cost + 1, (rp, cp), (dy, dx)))

    raise Exception


print(bfs())
