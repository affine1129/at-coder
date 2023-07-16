import sys

input = sys.stdin.readline

N = int(input())

S_list = [input()[:-1] for _ in range(N)] 
r_list = set()

for s in S_list:
    if s not in r_list and s[::-1] not in r_list:
        r_list.add(s)

print(len(r_list))
