import heapq

N, K = map(int, input().split())
S = input().strip()
heap = []
next_pos = 0
ans = ''

for i, c in enumerate(S):
    heapq.heappush(heap, (c, i))
    if N <= i + K:
        while True:
            d, j = heapq.heappop(heap)
            if next_pos <= j:
                next_pos = j + 1
                ans += d
                break

print(ans)

