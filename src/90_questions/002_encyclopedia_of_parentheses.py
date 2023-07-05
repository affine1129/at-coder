# 再帰的に解く
def main():
    N = int(input())
    if N % 2:
        print('')
    else:
        result_list = add_kakko(N, 0, 0)
        print('\n'.join(result_list))
   
def add_kakko(n, left, right):
    # 探索完了
    if n == left + right:
        return ['']

    # leftが全体の半分に到達した時、残りは全てright
    elif left == n/2:
        return add_right(n, left, right)
    # leftとrightの数が等しい時は必ずleft
    elif left == right:
        return add_left(n, left, right)
    # 上記以外の場合は、left, right共に考える
    else:
        return add_left(n, left, right) + add_right(n, left, right)

def add_left(n, left, right):
    return ['(' + kakko for kakko in add_kakko(n, left+1, right)]

def add_right(n, left, right):
    return [')' + kakko for kakko in add_kakko(n, left, right+1)]


# 全探索で解く
def sub_main():
    N = int(input())

    if N % 2 == 1:
        print('')
    else:
        result_list = []
        for i in range(2 ** N):
            l_count = 0
            r_count = 0
            bin_i = format(i, f'0{N}b')
            for j in bin_i:
                if j == '0':
                    l_count += 1
                elif j == '1':
                    r_count += 1
                else:
                    break

                if l_count < r_count:
                    break
                if l_count > N / 2 or r_count > N / 2:
                    break
            else:
                result_list.append(bin_i)

        result = '\n'.join(result_list)
        result = result.replace('0', '(')
        result = result.replace('1', ')')
        print(result)


if __name__ == '__main__':
    main()

