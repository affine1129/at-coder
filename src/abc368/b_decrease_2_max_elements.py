N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
    A = sorted(A, reverse=True)
    if A[1] == 0:
        break
    A[0] -= 1
    A[1] -= 1
    count += 1

print(count)
