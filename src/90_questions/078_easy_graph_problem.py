N, M = map(int, input().split())

graph = [set() for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    graph[A].add(B)
    graph[B].add(A)

ans = 0
for i in range(N):
    count = 0
    for j in graph[i]:
        if j < i:
            count += 1
    if count == 1:
        ans += 1

print(ans)
