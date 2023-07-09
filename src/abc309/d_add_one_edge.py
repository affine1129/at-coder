import sys

input = sys.stdin.readline

N1, N2, M = map(int, input().split())

a_b_list = [list(map(int, input().split())) for _ in range(M)]

def dfs():
    from heapq import heappop, heappush
    pass
