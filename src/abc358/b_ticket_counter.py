N, A = map(int, input().split())
T = list(map(int, input().split()))

time = 0
for t in T:
    if time <= t:
        time = t + A
    else:
        time += A
    print(time)
