N = int(input())

set_ = set()
for i in range(N):
    S = input()
    if S in set_:
        continue
    set_.add(S)
    print(i + 1)
