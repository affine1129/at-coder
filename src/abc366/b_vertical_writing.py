N = int(input())
S = [input() for _ in range(N)]

len_list = list(map(lambda x: len(x), S))
max_len_list = []
for i in range(N):
    max_len_list.append(max(len_list[:i + 1]))
max_len = max(len_list)
ans: list[str] = []
for i in range(0, max_len):
    str_: str = ''
    for j in range(N - 1, -1, -1):
        len_ = len(S[j])
        if len_ < i + 1:
            if i + 1 <= max_len_list[j] and len_ < max_len_list[j]:
                str_ += '*'
        else:
            str_ += S[j][i]
    ans.append(str_)

print('\n'.join(ans))
