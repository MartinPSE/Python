# 1. for문을 이용한 풀이

# def solution(prices):
#     answer = [0] * len(prices)
#
#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             if prices[i] <= prices[i + 1]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#
#     return answer


# print(solution([1, 2, 3, 2, 3]))
#-------------------------- 시간 초과 판정 ------------------------

# 2. Stack or Queue를 이용
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        count = 0
        c = prices.popleft()

        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)

    return answer

print(solution([1,2,3,2,3]))

# --- 나름 queue 를 써서 한 answer ---








































