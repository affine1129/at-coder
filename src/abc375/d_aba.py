from collections import Counter, defaultdict

S = input()

dict_ = defaultdict(int)
counter = Counter()
ans = 0
for s in S:
    ans += dict_[s]
    for k, v in counter.items():
        dict_[k] += v
    counter[s] += 1

print(ans)
