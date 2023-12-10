N = int(input())
A = list(set(map(int, input().split())))

A = sorted(A)

print(A[-2])
