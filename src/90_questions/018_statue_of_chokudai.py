import sys
import numpy as np

input = sys.stdin.readline


def get_theta(vec1: list, vec2: list) -> float:
    inner = np.inner(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return np.arccos(inner / (norm1 * norm2)) * 180 / np.pi


T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

ans = []
for i in range(Q):
    radian = E[i] * 2 * np.pi / T
    if radian == 0:
        ans.append('0')
        continue
    v = (np.cos(radian) * -1 + 1) * 0.5 * L
    h = np.sin(radian) * -0.5 * L
    vec1 = [X, abs(Y - h), 0]
    vec2 = [X, abs(Y - h), v]
    ans.append(str(get_theta(vec1, vec2)))

print('\n'.join(ans))
