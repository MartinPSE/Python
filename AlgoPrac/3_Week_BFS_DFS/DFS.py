# 깊이 우선 탐색
# Stack의 활용 예시

# 빈통 1개  / 검사 통 1개

# ex) 미로 찾기

# numpy 를 써서 2차원 배열을 만들거나
import numpy as np

stage = np.zeros([2,3])
print(stage)

# 간단한 반복문을 통해서 2차원 배열을 만들거나
N = 5 # row
M = 5 # column
stage = [[0] * M for i in range(N)]
print(stage)


