N, M, Q = map(int, input().split())
ABC = [tuple(map(int, input().split())) for _ in range(M)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

ex = set()
for q in queries:
    if q[0] == 1:
        ex.add(q[1] - 1)

MAX = 10 ** 18

mins = [[MAX] * N for _ in range(N)]
for i in range(N):
    mins[i][i] = 0
for i in range(M):
    if i in ex:
        continue
    A, B, C = ABC[i]
    A, B = A - 1, B - 1
    mins[A][B] = min(mins[A][B], C)
    mins[B][A] = min(mins[B][A], C)

for i in range(N):
    for j in range(N):
        for k in range(N):
            mins[j][k] = min(mins[j][k], mins[j][i] + mins[i][k])

ans = []
for i in range(Q - 1, -1, -1):
    q = queries[i]
    if q[0] == 1:
        A, B, C = ABC[q[1] - 1]
        A, B = A - 1, B - 1
        mins[A][B] = min(mins[A][B], C)
        mins[B][A] = min(mins[B][A], C)
        for j in range(N):
            for k in range(N):
                mins[j][k] = min(mins[j][k], mins[j][A] + mins[B][k] + C, mins[j][B] + mins[A][k] + C)
                mins[k][j] = min(mins[k][j], mins[k][A] + mins[B][j] + C, mins[k][B] + mins[A][j] + C)
    if q[0] == 2:
        x, y = q[1] - 1, q[2] - 1
        ans.append(-1 if mins[x][y] == MAX else mins[x][y])

for i in range(len(ans) - 1, -1, -1):
    print(ans[i])
