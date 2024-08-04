A, B = map(int, input().split())

max_ = max(A, B)
min_ = min(A, B)
for i in range(max_, (10**18) + 1, max_):
    if i % min_ == 0:
        print(i)
        break
else:
    print('Large')
