N = int(input())
X, Y = zip(*[list(map(int, input().split())) for _ in range(N)])

X = sorted(X)
Y = sorted(Y)

xmin = X[0]
xmax = X[-1]
ymin = Y[0]
ymax = Y[-1]

xcet = X[N // 2]
xans = sum(map(lambda x: abs(x - xcet), X))

ycet = Y[N // 2]
yans = sum(map(lambda y: abs(y - ycet), Y))

print(xans + yans)
