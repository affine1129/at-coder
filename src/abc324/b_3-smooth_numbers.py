N = int(input())

while True:
    if N == 1:
        print('Yes')
        break

    if N % 2 == 0:
        N = N / 2
    elif N % 3 == 0:
        N = N / 3
    else:
        print('No')
        break
    

