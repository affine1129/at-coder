import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
import numpy as np

input = sys.stdin.readline

N, M = map(int, input().split())

row, col = [], []
for _ in range(M):
    a, b = map(int, input().split())
    row.append(a - 1)
    col.append(b - 1)

data = np.ones(M, dtype=np.int64)

csr = csr_matrix((data, (row, col)), shape=(N, N))

num, scc = connected_components(csr, directed=True, connection='strong')
components, sizes = np.unique(scc, return_counts=True)
sizes = sizes[sizes >= 2]

if sizes.size == 0:
    print('0')
else:
    ans = 0
    for s in sizes:
        ans += s * (s - 1) // 2
    print(ans)
