from itertools import permutations
import math

'''
 #1. 소수 구하기 에라토스테네스의 체 --> 이해가 조금 안된다.

 def prime_list(n):
     # 에라토스테네스의 체 초기화 : n개 요소에 True 설정 (소수로 간주)
     sieve = [True] * n

     # n의 최대 약수가 sqrt(n) 이하 이므로 i = sqrt(n)까지 검사
     m = int(n ** 0.5)
     for i in range(2, m + 1):
         if sieve[i]:  # i가 소수인 경우
             for j in range(i + 1, n, i):  # i 이후 i의 배수들을 False 판정
                 sieve[j] = False
     # 소수 목록 산출
     return [i for i in range(2, n) if sieve[i] == True]

 #2. 에라토스테네스의 체 간단히 구현. 
 
 def solution(n):
     num = set(range(2, n + 1))
 

 for i in range(2, n + 1):
     if i in num:
         num -= set(range(2 * i, n + 1, i)

 return len(num)

    #3. 가볍게 구현
    def prime_list(n):
        if n < 2: return False
    
        to = int(math.sqrt(n)) + 1  # 제곱근 까지만 하면 된다 // 어차피
        for i in range(2, to):
            if n % i == 0: return False
        return True
'''


def prime_list(n):
    if n < 2: return False

    to = int(math.sqrt(n)) + 1
    for i in range(2, to):
        if n % i == 0: return False
    return True


def solution(numbers):
    val_set = set()  # 011 은 11과 똑같아.
    for i in range(1, len(numbers) + 1):  # numbers의 길이만큼 하자
        for val in list(map("".join, permutations(numbers, i))):  # itertools의 순열을 이용해서 수 조합을 짜보자.
            if prime_list(int(val)) is True:  # 소수냐?
                val_set.add(int(val))  # set()에 추가해주자!

    return len(val_set)  # set에 추가 된 갯수를 반환.


print(solution2("011"))
