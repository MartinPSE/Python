# 모의고사
from itertools import count

'''

dictionary 의 이용 . 
dict.values() --> value 값 도출 
dict.items() ---> key, value 를 
dict.keys() --> key 값 도출

dict { key : value }

'''


def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5]  # 5번
    b = [2, 1, 2, 3, 2, 4, 2, 5]  # 8번
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10번

    count_A = 0
    count_B = 0
    count_C = 0

    for i, v in enumerate(answers):
        if answers[i] == a[i % 5]:
            count_A += 1
        if answers[i] == b[i % 8]:
            count_B += 1
        if answers[i] == c[i % 10]:
            count_C += 1

        score_dict = {1: count_A, 2: count_B, 3: count_C}
        max_score = max(score_dict.values())

        student_score = score_dict.items()

        answer = [student for student,score in student_score if score == max_score]

    return print(answer)


solution([1, 3, 2, 4, 2])
