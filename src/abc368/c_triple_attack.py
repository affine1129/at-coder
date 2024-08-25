N = int(input())

H = list(map(int, input().split()))

mod = 2
T = 0
for h in H:
    while mod > 0 and h > 0:
        h -= 1
        mod -= 1
        T += 1

    tmp_mod = h % 5
    if 0 < tmp_mod <= 3:
        T += 1
        mod = 2
    elif tmp_mod == 4:
        T += 2
        mod = 1

    count = h // 5
    T += count * 3

print(T)
