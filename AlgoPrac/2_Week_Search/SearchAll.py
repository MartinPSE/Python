# 반복문과 재귀함수( 동적계획법, 백트래킹, 탐욕법 )
# 완전탐색 --> 반복문
# 길이까지 찾고, 원하는 값이 나오면 반환~
'''
# 재귀함수
무한루프를 주의하자!
def solution(trump, loc):
    if trump[loc]==8:
        return loc
    else:
        return solution(trump, loc+1)

solution 이 solution 을 호출한다.
'''

