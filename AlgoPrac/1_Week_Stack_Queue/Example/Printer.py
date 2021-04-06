from collections import deque


# 중요한 함수 enumerate
# enumerate( list, dict , .. ) --> 열거 해준다.

# 중요한 함수 ANY
# ANY ( ) --> 아무거나 TRUE면 바로 TRUE 리턴.

# < 인덱스 : value >

def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]  # 일단 index를 만들어놔야해 관리하기 편하게.
    answer = 0
    while True:  # 무한루프
        cur = queue.pop(0) # 비교를 위한 맨처음 수
        if any(cur[1] < q[1] for q in queue): # 그리고 하나하나 비교하고
            queue.append(cur) # 만약 원하는 수보다
        else:
            answer += 1
            if cur[0] == location:
                return answer


# location이 언제나오냐?


'''
1. 인덱스번호로 --> 책의 우선순위를 받는 Idea를 떠올려야해

2. 최종 출력될 인쇄물들을 순서대로 집어 넣자.


def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer



'''
