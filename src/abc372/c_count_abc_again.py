N, Q = map(int, input().split())
S = list('..' + input() + '..')

ABC = ['A', 'B', 'C']

ans = 0
for i in range(2, N + 2):
    ans += int(S[i:i + 3] == ABC)

for _ in range(Q):
    X, C = input().split()
    X = int(X) + 1

    for i in range(X - 2, X + 1):
        ans -= int(S[i: i + 3] == ABC)

    S[X] = C

    for i in range(X - 2, X + 1):
        ans += int(S[i: i + 3] == ABC)

    print(ans)
