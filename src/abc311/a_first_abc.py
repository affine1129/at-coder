N = int(input())
S = input()

a = S.index('A')
b = S.index('B')
c = S.index('C')

print(max([a, b, c]) + 1)
