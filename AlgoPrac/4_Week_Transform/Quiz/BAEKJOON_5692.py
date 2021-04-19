import sys
# number = int(sys.stdin.readline())
#
# print(number)
from sys import stdin

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


# print(len(number))
# print(type(number))

while (True):
    number = sys.stdin.readline().rstrip()
    if number == "0":
        break
    answer = 0
    for i in range(1, len(number) + 1):
        answer += int(number[len(number)-i]) * factorial(i)
    print(answer)


