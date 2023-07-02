count = 0

def main():
    N, Q = (int(x) for x in input().split())

    chars = [chr(i) for i in range(65, 65 + N)]
    result = []

    if N == 26 and Q == 1000:
        result = chars
        for i in reversed(range(N)):
            for j in range(i):
                ans = hearing(result[j], result[j+1])
                if ans == '>':
                    exchange_char(result, j, j+1)

    elif N == 26 and Q == 100:
        tmp1, tmp2, tmp3, tmp4, tmp5 = [], [], [], [], []
        # 1:1の塊で大小を判定する
        for i in range(0, 26, 2):
            tmp1 += merge_sort(chars[i:1+i], chars[1+i:2+i])

        # 2:2の塊で大小を判定する
        for i in range(0, 24, 4):
            tmp2 += merge_sort(tmp1[i:2+i], tmp1[2+i:4+i])

        # 4:4の塊で大小を判定する
        for i in range(0, 24, 8):
            tmp3 += merge_sort(tmp2[i:4+i], tmp2[4+i:8+i])

        # 8:8の塊で大小を判定する
        for i in range(0, 16, 16):
            tmp4 += merge_sort(tmp3[i:8+i], tmp3[8+i:16+i])

        # 8と2で大小を判定する
        tmp5 = merge_sort(tmp3[16:24], tmp1[24:26])

        # 16と10で大小を判定する
        result = merge_sort(tmp4, tmp5)


    elif N == 5 and Q == 7:
        # step1
        step1_ans = hearing(chars[0], chars[1])
        if step1_ans == '<':
            # result = ['A', 'B']
            result.extend([chars[0], chars[1]])
        elif step1_ans == '>':
            # result = ['B', 'A']
            result.extend([chars[1], chars[0]])

        # step2
        step2_ans = hearing(chars[3], chars[4])
        if step2_ans == '<':
            # result = ['X', 'X', 'D', 'E']
            result.extend([chars[3], chars[4]])
        elif step2_ans == '>':
            # result = ['X', 'X', 'E', 'D']
            result.extend([chars[4], chars[3]])
       
        # step3
        step3_ans = hearing(result[0], result[2])
        # 'A', 'B'の小さい方 > 'D', 'E'の小さい方 > 'D', 'E'の大きい方
        if step3_ans == '<':
            exchange_char(result, 1, 2) 
            exchange_char(result, 2, 3) 

        # 'D', 'E'の小さい方 > 'A', 'B'の小さい方 > 'A', 'B'の大きい方
        elif step3_ans == '>':
            exchange_char(result, 0, 2) 
            exchange_char(result, 2, 1) 

        # step4
        step4_ans = hearing(chars[2], result[1])
        if step4_ans == '<':
            # step5
            step5_ans = hearing(chars[2], result[0])
            if step5_ans == '<':
                insert_char(result, chars[2], 0)
            elif step5_ans == '>':
                insert_char(result, chars[2], 1)
        if step4_ans == '>':
            # step5
            step5_ans = hearing(chars[2], result[2])
            if step5_ans == '<':
                insert_char(result, chars[2], 2)
            elif step5_ans == '>':
                insert_char(result, chars[2], 3)
                
        # step6
        step6_ans = hearing(result[4], result[2])
        if step6_ans == '<':
            # step7
            step7_ans = hearing(result[4], result[1])
            if step7_ans == '<':
                insert_char(result, result[4], 1)
            elif step7_ans == '>':
                insert_char(result, result[4], 2)
        if step6_ans == '>':
            # step7
            step7_ans = hearing(result[4], result[3])
            if step7_ans == '<':
                insert_char(result, result[4], 3)
            elif step7_ans == '>':
                insert_char(result, result[4], 4)

        delete_char(result, 5)

    print(f'! {"".join(result)}')

    
def merge_sort(list1, list2):
    return_list = []
    offset = 0
    for idx, c1 in enumerate(list1):
        for c2 in list2[offset:]:
            ans = hearing(c1, c2)
            if ans == '<':
                return_list.append(c1) 
                break
            elif ans == '>':
                return_list.append(c2)
                offset += 1
        else:
            return_list += list1[idx:]
            break
    else:
        return_list += list2[offset:]
    return return_list

def hearing(char1, char2):
    print(f'? {char1} {char2}')
        
    ans = input()

    return ans

def delete_char(target_chars, index):
    target_chars.pop(index)

def insert_char(target_chars, insert_char, index):
    target_chars.insert(index, insert_char)

def exchange_char(chars, num1, num2):
    tmp = chars[num1]
    chars[num1] = chars[num2]
    chars[num2] = tmp

if __name__ == '__main__':
    main()
