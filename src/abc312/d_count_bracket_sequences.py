import sys
sys.setrecursionlimit(10**6)

MOD = 998244353

S = input()
N = len(S)

ans = 0
def dfs(idx, count):
    for i in range(idx, N):
        if count < 0:
            return 0

        if S[i] == '?':
            dfs(i+1, count-1)
            dfs(i+1, count+1)
            return
        elif S[i] == '(':
            count += 1
        else:
            count -= 1

    if count == 0:
        global ans
        ans += 1 
        ans %= MOD

dfs(0, 0)
print(ans)

