N, D = map(int, input().split())

X: list[int] = []
Y: list[int] = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

x_max = max(map(abs, X))
y_max = max(map(abs, Y))

x_ini = -(x_max + D)
y_ini = -(y_max + D)
xd = [0] * (abs(x_ini * 2) + 1)
yd = [0] * (abs(y_ini * 2) + 1)

for n in range(N):
    xd[x_ini] += abs(X[n] - x_ini)
    yd[y_ini] += abs(Y[n] - y_ini)

cur_i = 0
for x in range(x_ini + 1, abs(x_ini) + 1):
    while cur_i < N and X[cur_i] < x:
        cur_i += 1
    xd[x] = xd[x - 1] + cur_i - (N - cur_i)

cur_i = 0
for y in range(y_ini + 1, abs(y_ini) + 1):
    while cur_i < N and Y[cur_i] < y:
        cur_i += 1
    yd[y] = yd[y - 1] + cur_i - (N - cur_i)

xd.sort(reverse=True)
yd.sort()

ans = 0
index = 0
yd_len = len(yd)
for x in xd:
    diff = D - x
    while index < yd_len and yd[index] <= diff:
        index += 1
    ans += index

print(ans)
