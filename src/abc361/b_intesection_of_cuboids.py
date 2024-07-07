a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

flg = True
if d <= g or e <= h or f <= i:
    flg = False
elif j <= a or k <= b or l <= c:
    flg = False

print('Yes' if flg else 'No')
