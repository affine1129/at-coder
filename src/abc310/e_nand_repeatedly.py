N = int(input())
S = input()

count, zero, one = 0, 0, 0
for i in S:
    if i == '0':
        zero, one = 1, zero + one
    else:
        zero, one = one, zero + 1
    count += one

print(count)


