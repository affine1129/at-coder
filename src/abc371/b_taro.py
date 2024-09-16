N, M = map(int, input().split())

ls = [False] * N
for _ in range(M):
    A, B = input().split()
    A = int(A) - 1
    if not ls[A] and B == 'M':
        print('Yes')
        ls[A] = True
    else:
        print('No')
