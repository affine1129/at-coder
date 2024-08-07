TARGET = 46

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a_mod, b_mod, c_mod = [0] * TARGET, [0] * TARGET, [0] * TARGET
for a, b, c in zip(A, B, C):
    a_mod[a % TARGET] += 1
    b_mod[b % TARGET] += 1
    c_mod[c % TARGET] += 1

ans = 0
for a in range(TARGET):
    for b in range(TARGET):
        for c in range(TARGET):
            if (a + b + c) % TARGET == 0:
                ans += a_mod[a] * b_mod[b] * c_mod[c]


print(ans)
