H, W = map(int, input().split())

import numpy as np
A = np.array([list(map(int, input().split())) for _ in range(H)])

result_list = np.array(list(map(lambda x: list(map(lambda y: y * -1, x)), A)))

result_list += np.sum(A, axis=0)

result_list += np.array([np.sum(A, axis=1)]).T

for i in range(len(result_list)):
    print(' '.join(map(str, result_list[i])))
