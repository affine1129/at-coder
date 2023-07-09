N = int(input())

A = [[ i for i in input() ] for _ in range(N)]

B = [[ i for i in a ] for a in A ]

for i in range(len(A)-1):
    B[0][i+1] = A[0][i]

for i in range(len(A)-1):
    B[i+1][N-1] = A[i][N-1]

for i in range(len(A)-1):
    B[N-1][N-i-2] = A[N-1][N-i-1]

for i in range(len(A)-1):
    B[N-i-2][0] = A[N-i-1][0]

for b in B:
    print(''.join(b))

