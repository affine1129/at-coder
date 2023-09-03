import heapq

def main():
    N, M = map(int, input().split())
    roads = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        roads[a].append((b, c))
        roads[b].append((a, c))


    def dijlstra(x):
        q = []
        dist = [10 ** 9] * N
        dist[x] = 0
        # (start, cost)のtuple
        heapq.heappush(q, (0, x))
        while len(q) > 0:
            cur_cost, now = heapq.heappop(q)
            if cur_cost > dist[now]:
                continue
            for to, cost in roads[now]:
                if cost + cur_cost < dist[to]:
                    dist[to] = cost + cur_cost 
                    heapq.heappush(q, (cost + cur_cost, to))

        return dist


    from_1 = dijlstra(0)
    from_k = dijlstra(N-1)

    for n in range(N):
        print(from_1[n] + from_k[n])

if __name__ == "__main__":
    main()
