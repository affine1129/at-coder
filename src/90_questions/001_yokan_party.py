# 二部探索を使用
def main():
    def check(x, N, L, K, A):
        start_point = 0
        cut_num = 0
        for n in range(N):
            if A[n] - start_point >= x:
                start_point = A[n]
                cut_num += 1
        if L - start_point >= x:
            cut_num += 1

        return cut_num >= K + 1

    N, L = (int(x) for x in input().split())
    K = int(input())
    A = [int (x) for x in input().split()]

    left, right = -1, L + 1
    while right - left > 1:
        mid = (right + left) // 2
        if check(mid, N, L, K, A):
            left = mid
        else:
            right = mid
    print(left)


def pre_main():
    N, L = (int(x) for x in input().split())
    K = int(input())
    A_list = [int (x) for x in input().split()]

    modified_a = [0] + A_list + [L]
    target_size = L / 2
    min_size = target_size
    cutting_points = [0, -1]
    cur_cut_points = [0, -1]

    for k in range(K):
        # どの長さから始まるかを取得する
        start_point = modified_a[cur_cut_points[0]]

        # 対象のようかんのうち、半分により近い切れ目を求める
        for idx, a in enumerate(modified_a[cur_cut_points[0]:cur_cut_points[1]]):
            if min_size >= abs((start_point + target_size) - a):
                min_size = abs((start_point + target_size) - a)
            else:
                cutting_points.append(idx-1)
                break

        # 切ることが確定した切れ目のリストから一番大きいようかんを決定する
        max_size = 0
        for idx, point in enumerate(cutting_points):
            if max_size < modified_a[point] - modified_a[point-1]:
                max_size = modified_a[point] - modified_a[point-1]
                cur_cut_points = [point, cutting_points[idx-1]]
        target_size = max_size

    # 切れ目から最小のようかんを求める
    cutting_points.sort()
    cutting_points = cutting_points[1:] + [-1]
    score = min([modified_a[i] - modified_a[cutting_points[idx]] for idx, i in enumerate(cutting_points[1:])])
    print(score)

if __name__ == '__main__':
    main()

