def dfs_main():
    N = int(input())
    d = [[0] * N for _ in range(N)]
    for i in range(N-1):
        D = list(map(int, input().split()))
        for j in range(i+1, N):
            d[i][j] = d[j][i] = D[j-i-1]

    def dfs(used):
        if all(used):
            return 0
        x = used.index(False)
        used[x] = True
        ret = 0
        for i in range(x+1, N):
            if not used[i]:
                used[i] = True
                ret = max(ret, d[x][i] + dfs(used))
                used[i] = False
        used[x] = False
        return ret


    used = [False] * N
    ans = 0
    if N % 2 == 1:
        for i in range(N):
            used[i] = True
            ans = max(ans, dfs(used))
            used[i] = False
            
    else:
        ans = dfs(used)

    print(ans)

def bit_main():
    N = int(input())
    d = [[0] * N for _ in range(N)]
    for i in range(N-1):
        D = list(map(int, input().split()))
        for j in range(i+1, N):
            d[i][j] = D[j-i-1]

    dp = [0] * (2 ** N)
    for i in range(2 ** N - 1):
        idx = -1
        for j in range(N):
            if not (i >> j & 1):
                # 検索する箇所
                idx = j
                break

        for j in range(idx+1, N):
            if (i >> j & 1):
                continue
            nex = (1 << idx) | (1 << j) | i
            dp[nex] = max(dp[nex], d[idx][j] + dp[i])

    print(dp[2 ** N - 1])


if __name__ == '__main__':
    bit_main()

