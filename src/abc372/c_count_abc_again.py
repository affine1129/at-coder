N, Q = map(int, input().split())
S = list('..' + input() + '..')

ans = 0
index = set()
pre_a = pre_b = False
for i, s in enumerate(S):
    if s == 'A':
        pre_a = True
        pre_b = False
        continue
    elif pre_a and s == 'B':
        pre_b = True
        pre_a = False
        continue
    elif pre_b and s == 'C':
        ans += 1
        index.add(i - 2)
    pre_a = pre_b = False

for _ in range(Q):
    X, C = input().split()
    X = int(X) + 1

    if C == S[X]:
        print(ans)
        continue

    if X in index:
        index.remove(X)
        ans -= 1
    elif (X - 1) in index:
        index.remove(X - 1)
        ans -= 1
    elif (X - 2) in index:
        index.remove(X - 2)
        ans -= 1

    if C == 'A':
        ans += int(S[X + 1] == 'B' and S[X + 2] == 'C')
        index.add(X)
    elif C == 'B':
        ans += int(S[X - 1] == 'A' and S[X + 1] == 'C')
        index.add(X - 1)
    elif C == 'C':
        ans += int(S[X - 2] == 'A' and S[X - 1] == 'B')
        index.add(X - 2)

    S[X] = C

    print(ans)
