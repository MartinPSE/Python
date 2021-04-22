participant = ["leo", "kiki", "eden"]

completion = ["eden", "kiki"]

# 너무 단순하게 생각했다, 중복이 있다는 걸 생각 못했다.
# answer = ""
# for part in participant:
#     if part not in completion:
#         answer = part

# Counter 함수를 이용하자!
# 배열안에 있는 변수들의 { 개수 : 변수 } 로 dict형태로 묶어 준다.

from collections import Counter

def solution(participant,completion):
    answer = list((Counter(participant)-Counter(completion)).keys())[0]

    return print(answer)

solution(participant,completion)

