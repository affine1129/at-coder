N = int(input())
n_list = [list(map(int, input().split())) for _ in range(N - 1)]
d_list = [[] for _ in range(N)] 
for n in n_list:
    d_list[n[0]-1].append(n[1]-1)
    d_list[n[1]-1].append(n[0]-1)

def dfs(num):
    stack = [num]
    result_list = [-1] * N
    result_list[num] = 1
    while stack:
        num = stack.pop()
        for d in d_list[num]:
            if result_list[d] != -1: continue
            stack.append(d)
            result_list[d] = result_list[num] + 1

    return result_list

result_list = dfs(0)
max_node = result_list.index(max(result_list))
result_list = dfs(max_node)
print(max(result_list))
