M = int(input())
S1 = input()
S2 = input()
S3 = input()


def search(ss, c):
    index = 0
    try:
        for s in ss:
            index = s[index:].index(c) + 1 + index 
        return index - 1
    except ValueError:
        return 10**9


set1 = {c for c in S1}
set2 = {c for c in S2}
set3 = {c for c in S3}

tar = set1 & set2 & set3

ans = 0
if len(tar) == 0:
    ans = -1
else:
    S1 = S1*3
    S2 = S2*3
    S3 = S3*3
    ans = 10**9
    for i in tar:
        ans = min(
            search([S1, S2, S3], i), 
            search([S1, S3, S2], i),
            search([S2, S1, S3], i),
            search([S2, S3, S1], i),
            search([S3, S1, S2], i),
            search([S3, S2, S1], i),
            ans
        ) 

print(ans)
