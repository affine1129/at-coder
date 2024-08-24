A, B, C = map(int, input().split())

if (B < C and (A < B or C < A)) or (C < B and (A < B and C < A)):
    print('Yes')
else:
    print('No')
