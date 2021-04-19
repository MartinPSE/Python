# 1~100 사이 숫자 중 랜덤으로 10개 뽑아서 리스트 만들기
import random

numbers = []
for i in range(1, 10):
    number = random.randint(1, 101)
    numbers.append(number)
print(numbers)

# 랜덤리스트 내의 숫자 중 최대값, 최소값 구하기
import sys

min = sys.maxsize
max = -sys.maxsize
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]
print(f"최대값은 {max}이고 최소값은 {min}입니다")
