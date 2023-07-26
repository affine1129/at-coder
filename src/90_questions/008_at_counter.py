N = int(input())
S = input()

MOD = 10 ** 9 + 7

set_ = {'a', 't', 'c', 'o', 'd', 'e', 'r'}
str_ = 'atcoder'
list_ = [0] * 7
for s in reversed(S):
    if s == 'r':
        list_[0] += 1
    elif s in set_:
        pos = 6 - str_.index(s)
        list_[pos] += list_[pos-1]
        list_[pos] %= MOD

print(list_[-1])
