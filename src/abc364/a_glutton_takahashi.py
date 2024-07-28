N = int(input())

pre = ''
cur = ''
ng = False
for _ in range(N):
    S = input()
    cur = S
    if ng:
        print('No')
        break
    if cur == 'sweet' and pre == 'sweet':
        ng = True
    pre = cur
else:
    print('Yes')
