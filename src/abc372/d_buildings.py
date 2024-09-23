from collections import Counter

N = int(input())
H = list(map(int, input().split()))

counter = Counter()
ls = [0] * N
for i in range(N):
    ls[i] = sum([counter[j] for j in range(1, H[i] + 1)])
    counter[H[i]] += 1

print(counter)
print(*ls)

ans = [ls[-1] - ls[i] for i in range(N)]
print(*ans)
