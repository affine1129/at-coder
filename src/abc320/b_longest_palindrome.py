import sys
sys.setrecursionlimit(10**6)

S = input()

def dfs(s):
    if s == s[::-1]:
        return len(s)
    else:
        return max(dfs(s[1:]), dfs(s[:-1]))

ans = 0
sl = len(S)
for i in range(sl-1):
    count = 1
    for j in range(1, min(sl-i, i+1)):
        if S[i-j] == S[i+j]:
            count += 2
        else:
            break
    ans = max(count, ans)

    if S[i] == S[i+1]: 
        count = 2
        for j in range(1, min(sl-i-1, i+1)):
            if S[i-j] == S[i+j+1]:
                count +=2
            else:
                break
        ans = max(count, ans)
                 
print(ans)
