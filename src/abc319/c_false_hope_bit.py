import sys

input = sys.stdin.readline

C = list(map(int, input().split())) + list(map(int, input().split())) + list(map(int, input().split()))
sum_ = 362880

dp = [0] * 512

for i in range(512):
    for j in range(3):
        for k in range(3):
            for target1, target2, target3 in [
                    (j*3+(k%3), j*3+((k+1)%3), j*3+((k+2)%3)),
                    (j+(k%3*3), j+((k+1)%3*3), j+((k+2)%3*3)),
                ]:
                if C[target1]==C[target2] and ((i>>target1)&(i>>target2)&1)==1 and ((i>>target3)&1)==0:
                    dp[i] = -1

        for target1, target2, target3 in [
                (j%3*4, (j+1)%3*4, (j+2)%3*4),
                ((j%3+1)*2, ((j+1)%3+1)*2, ((j+2)%3+1)*2),
            ]:
            if C[target1]==C[target2] and ((i>>target1)&(i>>target2)&1)==1 and ((i>>target3)&1)==0:
                dp[i] = -1


dp[0] = 1
for i in range(512):
    if dp[i] == -1:
        continue
    for j in range(9):
        if (i>>j)&1 == 0 and dp[i|(1<<j)] != -1:
            dp[i|(1<<j)] += dp[i]

print(dp[511] / sum_)

