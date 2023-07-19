#  import numpy as np
N, B, _ = map(int, input().split())
mod = 10 ** 9 + 7

c_list = list(map(int, input().split()))


# dpに対して繰り返し二乗法を使用する
def question3():
    def vec_mul(a_list, b_list, exp):
        ret = [0] * B
        for i in range(B):
            for j in range(B):
                next = (i * ten[exp] + j) % B
                ret[next] += a_list[i] * b_list[j]
                ret[next] %= mod
        return ret

    from itertools import accumulate

    # 10の累乗をBで割った余りのリストを取得する
    *ten, = accumulate(range(10, 72), lambda acc, _: (acc ** 2) % B)

    # 初期化
    doubled = [0] * B
    for c in c_list:
        doubled[c % B] += 1

    # 最初の1回を計算する
    global N
    if N & 1:
        ans = doubled
    else:
        ans = [0] * B
        # 2回目以降の計算に影響を与えないよう、先頭にのみ0を代入する
        ans[0] = 1
    N >>= 1

    exp = 0
    while N:
        doubled = vec_mul(doubled, doubled, exp) 
        exp += 1
        if N & 1:
           ans = vec_mul(ans, doubled, exp) 
        N >>= 1

    print(ans[0])


# 行列に対して繰り返し二乗法を使用する
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
        for j in range(len(b[0])):
            ret_mat[i][j] = sum([ x * y % mod for x, y in zip(a[i], [i[j] for i in b])]) % mod

    return ret_mat

if __name__ == '__main__':
    question3()
