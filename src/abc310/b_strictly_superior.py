import sys

input = sys.stdin.readline

N, M = map(int, input().split())

list_ = [list(map(int, input().split())) for _ in range(N)]

for p1, c1, *f_list1 in list_:
    for p2, c2, *f_list2 in list_:
        if p1 > p2:
            if set(f_list1) <= set(f_list2):
                print('Yes')
                exit()
        if p1 == p2:
            if set(f_list1) < set(f_list2):
                print('Yes')
                exit()
else:
    print('No')
