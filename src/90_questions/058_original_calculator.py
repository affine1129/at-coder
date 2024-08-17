N, K = map(int, input().split())

MOD = 10 ** 5

log = []
nums = set()
num = N
for _ in range(K):
    sum_ = sum(map(int, list(str(num))))
    num = (sum_ + num) % MOD
    if num in nums:
        break
    nums.add(num)
    log.append(num)

index1 = log.index(num)
index2 = len(log)
target = (K - index1 - 1) % (index2 - index1)
print(log[index1 + target])
