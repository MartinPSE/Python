'''


set써도된다. set 은 append가 아니라 add로 elements들 추가!

#1

from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))

#2

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)




'''

# 나는 요종도로 했는데 // itertools의 combination을 이용하게 되면 훨씬더 깔끔한 풀이가 가능하다.
#
# def solution(numbers):
#     answer = set()
#
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#                answer.add(numbers[i]+ numbers[j])
#
#
#
#
#     return sorted(answer)
#
# solution([2, 1, 3, 4, 1])

from itertools import combinations


def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
