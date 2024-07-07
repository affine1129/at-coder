from collections import deque

N = int(input())
S = input() + '..'
T = input() + '..'

result = {S: 0}
queue = deque([S])
while queue:
    tar = queue.popleft()
    if tar == T:
        print(result[tar])
        break
    empty = tar.find('.')
    for n in range(N + 1):
        if not (tar[n] == '.' or tar[n + 1] == '.'):
            tmp = tar
            tmp = tmp.replace('..', tmp[n:n + 2])
            tmp = tmp[:n] + '..' + tmp[n + 2:]
            if tmp not in result:
                result[tmp] = result[tar] + 1
                queue.append(tmp)
else:
    print(-1)
