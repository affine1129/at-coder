from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

S = ''.join([input() for _ in range(H)])

directions = [W, -W, 1, -1]
costs = [-1] * (H * W)

start = (rs - 1) * W + (cs - 1)
goal = (rt - 1) * W + (ct - 1)


def bfs() -> int:
    def is_exist(pos: int, dir: int) -> bool:
        return not (
            pos >= ((H - 1) * W) and dir == directions[0] or
            pos < W and dir == directions[1] or
            (pos + 1) % W == 0 and dir == directions[2] or
            pos % W == 0 and dir == directions[3]
        )

    q: deque[tuple[int, int, int]] = deque([(0, start, d) for d in directions])
    while q:
        cost, pos, d = q.popleft()
        while True:
            if not is_exist(pos, d) or S[pos + d] == '#':
                break
            pos += d
            if pos == goal:
                return cost
            if costs[pos] != -1:
                continue
            costs[pos] = cost
            for dir in directions:
                if dir == d:
                    continue
                q.append((cost + 1, pos, dir))

    raise Exception


print(bfs())
