# print(ord('A') - 55)
# import sys
#
# number, M = sys.stdin.readline().split()
#
# print(number, M)
#
# print(type(ord(number[0]) - 55))  # z를 숫자로 바꾸자
#
# answer = 0
# for i in range(len(number) - 1, -1, -1):  # 4 3 2 1 0
#     answer += (ord(number[i]) - 55) * (int(M) ** abs(4 - i))
# print(answer)

# 런타임 에러가 났다.

n, x = input().split() # ZZZZZ 36
print(int(n, int(x)))


# 이게 끝이네..
# int는 A-Z 까지 10-35 까지 내장되어있다 자동적으로.