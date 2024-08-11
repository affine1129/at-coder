import bisect

N, K, P = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[:N // 2]
A2 = A[N // 2:]

a1_list: list[list[int]] = [[] for _ in range(K + 1)]
a2_list: list[list[int]] = [[] for _ in range(K + 1)]

a1_list[0].append(0)
for a1 in A1:
    for j in range(K, 0, -1):
        for pre_a1 in a1_list[j - 1]:
            a1_list[j].append(pre_a1 + a1)

a2_list[0].append(0)
for a2 in A2:
    for j in range(K, 0, -1):
        for pre_a2 in a2_list[j - 1]:
            a2_list[j].append(pre_a2 + a2)

for k in range(1, K + 1):
    a1_list[k] = sorted(a1_list[k])
    a2_list[k] = sorted(a2_list[k])

ans = 0
for i in range(len(a1_list)):
    a2_index = K - i
    for a1 in a1_list[i]:
        a2_val = P - a1
        ans += bisect.bisect_right(a2_list[a2_index], a2_val)

print(ans)
