import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = [input() for _ in range(N)]

def check(i, j):
    for r in range(1, 4):
        for c in range(1, 4):
            if r == 3 or c == 3:
                if S[i+r][j+c] != '.':
                    return False
            else:
                if S[i+r][j+c] != '#':
                    return False

    for r in range(5, 9):
        for c in range(5, 9):
            if r == 5 or c == 5:
                if S[i+r][j+c] != '.':
                    return False
            else:
                if S[i+r][j+c] != '#':
                    return False

    return True

ans = []
for i in range(N-8):
    for j in range(M-8):
        if S[i][j] == '#':
            if check(i, j):
                ans.append(f'{str(i+1)} {str(j+1)}')

print('\n'.join(ans))
            
