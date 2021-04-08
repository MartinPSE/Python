import math


# N이 소수인지 아닌지 판별하기 !

def prime_number(n):
    if n < 2:  # 1이니깐 소수 아니죠?
        return False
    to = int(math.sqrt(n)) + 1  # 제곱수는 소수가 아니니깐
    for i in range(2, to):  # 자기 자신과 1빼곤 약수로 가지면 안되죠?
        if n % i == 0: return False  # 그러면 False
    return True  # 소수네요 True를 반환.


# N 이하의 소수 구하는 방법

def prime_numbers(n):
    num = set(range(2, n + 1))  # 2 ~ n 까지의 수를 num에 넣자

    for i in range(2, n + 1):  # i의 배수를 num 에서 제거해주자
        if i in num:
            num -= set(range(2 * i, n + 1, i))

    return len(num)  # 남은 num 은 소수의 갯수.


'''
 N 까지의 소수를 구하는 방법.
 
 1. 2~n 까지의 수를 함수 num에 담고
 2. 2~n 까지의 수 i에 대해, i가 num 안에 있으면,
    i의 배수 set(i의 2배수 부터 n까지수 중 i만큼 간격있는 수를)
    num 에서 빼주기
 3. 나머지 num의 길이 리턴.
 
'''

'''
join() : 문자열 String 합치자 (int는 합칠 수 없어)
''.join() --> 공백없이 하나의 문자
','.join() --> ,로 합치기

split(인자) : 인자로 문자열을 나눌기준 설정
split(" ") --> 공백기준으로 문자 나눠줌
split(",") --> , 기준으로 문자 나눠줌
 

map(함수, iterable) : 함수(f)와 반복가능한(iterable) 자료형
                     iterable을 함수가 반복한 결과 Return
list(map(함수,리스트)) --> list로 감싸줘야 반환 
                    * 아니면 위치만 반환해준다.


'''

