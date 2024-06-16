import copy

N, M = map(int, input().split())
S = [input() for _ in range(N)]


def solve(num, set_, bits) -> set[int]:
    ret = set()
    if num == 1:
        for i in set_:
            ret.add(bits[i])
    else:
        for i in set_:
            cp_list = copy.deepcopy(set_)
            cp_list.remove(i)
            ret_list = solve(num - 1, cp_list, bits)
            ret = set(map(lambda x: x | bits[i], ret_list))
    return ret


bits = []
for s in S:
    num = 0
    for i, c in enumerate(s):
        if c == 'o':
            num += 2 ** i
    else:
        bits.append(num)

goal = 2 ** M - 1
for n in range(1, N + 1):
    max_ = max(solve(n, set(range(N)), bits))
    if max_ == goal:
        print(n)
        break
