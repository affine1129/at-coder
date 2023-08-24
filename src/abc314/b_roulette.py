import sys

input = sys.stdin.readline

N = int(input())

A_list = []
C_list = []
for _ in range(N):
   C = int(input())
   C_list.append(C)
   A_list.append(set(map(int, input().split())))

X = int(input())

ans = []
min = 37
for idx, a in enumerate(A_list):
    if X in a:
        if C_list[idx] < min: 
            min = C_list[idx]
            ans.clear()
            ans.append(idx+1)
        elif C_list[idx] == min:
            ans.append(idx+1)

ans.sort()

print(len(ans))
print(' '.join(list(map(lambda x: str(x), ans))))

