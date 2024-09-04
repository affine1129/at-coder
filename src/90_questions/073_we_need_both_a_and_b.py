N = int(input())
C = list(input().split())
MOD = 10 ** 9 + 7

tree = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    tree[A].append(B)
    tree[B].append(A)

dp = [[0] * 3 for _ in range(N)]
seen = [False] * N


def dfs(cur: int):
    seen[cur] = True

    index = int(C[cur] == 'b')
    prod = 1
    prod_ab = 1
    for nex in tree[cur]:
        if seen[nex]:
            continue

        dfs(nex)

        nex_dp = dp[nex]
        prod *= (nex_dp[index] + nex_dp[2])
        prod_ab *= (nex_dp[0] + nex_dp[1] + nex_dp[2] * 2)
        prod %= MOD
        prod_ab %= MOD

    dp[cur][index] = prod
    dp[cur][2] = (prod_ab - prod) % MOD


dfs(0)

print(dp[0][2])
