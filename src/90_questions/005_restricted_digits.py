#  import numpy as np

N, B, _ = map(int, input().split())
mod = 10 ** 9 + 7

c_list = list(map(int, input().split()))


def question2():
    matrix = [[0] * B for _ in range(B)]
    dot_matrix = [[1 if i == j else 0 for j in range(B)] for i in range(B)]

    for b in range(B):
        for c in c_list:
            matrix[b][(b * 10 + c) % B] += 1

    global N
    while N:
        if N & 1:
            dot_matrix = mat_mul(dot_matrix, matrix)
        matrix = mat_mul(matrix, matrix)
        N >>= 1

    print(dot_matrix[0][0])

def question1():
    dp = [[0 for _ in range(B)] for _ in range(N+1)]

    dp[0][0] = 1
    # 1桁目に数字をinsertしていくイメージ
    for n in range(N):
        for b in range(B):
            for c in c_list:
                dp[n+1][(b * 10 + c) % B] += dp[n][b] 
                dp[n+1][(b * 10 + c) % B] %= mod

    print(dp[N][0])

def mat_mul(a, b):
    ret_mat = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret_mat[i][j] = sum([ x * y % mod for x, y in zip(a[i], [i[j] for i in b])]) % mod

    return ret_mat

if __name__=='__main__':
    question2()
