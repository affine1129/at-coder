import sys

input = sys.stdin.readline

N = int(input())
A = set(input().split())

if len(A) == 1:
    print('Yes')
else:
    print('No')

