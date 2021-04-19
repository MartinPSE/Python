def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n,"0")
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        return answer
'''
처음에 너무 어렵게 접근해서
시간을 많이 잡아먹었다.
배열만 만드는게 중요한게 아니라.
결론을 간략하게 도출하는 것을 생각해보기.
'''


# 함수 : zip(*iterable)(iterable, 반복가능한 자료형 여러개)
# 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 한다.

# rjust 함수 ( ljust 도 마찬가지 )
# 문자열.rjust(전체 자리 숫자, 공백이 있을 경우 공백을 채울 텍스트)
# 기가막힌 함수군요, 공백을 그대로 두려면 아무것도 입력하지말기.

# # 비트연산자 or(|) 를 이용하여 한방에 구해버리고, 0b를 날려버리자.
# str(bin(a | b )) 발상의 전환.


