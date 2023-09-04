import time
import numpy as np

# 時間計測開始
time_sta = time.time()

# 処理を書く
list_ = np.array([0] * (10 ** 5))

for i in range(10 ** 5):
    list_[i] += 1

# 時間計測終了
time_end = time.time()
# 経過時間（秒）
tim = time_end - time_sta

print(tim)
