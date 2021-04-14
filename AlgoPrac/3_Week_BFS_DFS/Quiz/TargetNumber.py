from collections import deque

numbers = [1, 1, 1, 1, 1]

target = 3


# 1. queue를 이용해서
'''
통과 (858.60ms, 116MB)
테스트 2 〉	통과 (853.50ms, 116MB)
테스트 3 〉	통과 (0.77ms, 10.2MB)
테스트 4 〉	통과 (2.60ms, 10.6MB)
테스트 5 〉	통과 (17.49ms, 13.2MB)
테스트 6 〉	통과 (1.39ms, 10.3MB)
테스트 7 〉	통과 (0.79ms, 10.3MB)
테스트 8 〉	통과 (5.07ms, 10.7MB)
'''
#
# def solution(numbers, target):
#     answer = 0
#     queue = deque()
#     n = len(numbers)
#     queue.append([numbers[0], 0])
#     queue.append([-1 * numbers[0], 0])
#     while queue:
#         print(queue)
#         temp, idx = queue.popleft()
#         idx += 1
#         if idx < n:
#             queue.append([temp + numbers[idx], idx])
#             queue.append([temp - numbers[idx], idx])
#         else:
#             if temp == target:
#                 answer += 1
#     return answer

# print(solution(numbers, target))

# 2. stack 을 이용해서
''' 시간비교
통과 (419.24ms, 10.3MB)
테스트 2 〉	통과 (419.19ms, 10.3MB)
테스트 3 〉	통과 (0.76ms, 9.98MB)
테스트 4 〉	통과 (2.22ms, 10.2MB)
테스트 5 〉	통과 (13.24ms, 10.2MB)
테스트 6 〉	통과 (1.33ms, 10.2MB)
테스트 7 〉	통과 (0.70ms, 10.3MB)
테스트 8 〉	통과 (3.68ms, 10.3MB)
'''
def solution(numbers, target):
    answer = 0
    stack = []
    stack.append([numbers[0], 0])
    stack.append([-1 * numbers[0], 0])
    n = len(numbers)
    while stack:
        print(stack)
        temp, idx = stack.pop()
        idx += 1
        if idx < n:
            stack.append([temp + numbers[idx], idx])
            stack.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1

    return answer


print(solution(numbers, target))
