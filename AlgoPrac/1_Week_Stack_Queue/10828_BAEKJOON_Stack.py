# 10828 스택

'''
push X : 정수 X를 스택에 넣는 연산
pop : 스택에서 가장 위에있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우 -1 출력
size : 스택에 들어있는 정수의 개수를 출력
empty : 스택이 비어있으면 1, 아니면 0을 출력
top : 스택의 가장 위에 있는 정수를 출력, 만약 스택에 들어있는 정수가 없는 경우 -1 출력

import sys

sys.stdin.readLine() --> 한 줄 단위로 입력 받는다.

sys.stdin.readline.split() --> 한줄에 입력받은 문자열을 나눠준다.
ex) list(map(int,sys.stdin.readline().split()))

# 빈 list를 확인하려면
    >> if not list명 을 사용하자!

'''

import sys
N = int(sys.stdin.readline())

stack = list()

for i in range(N):
    cmd = sys.stdin.readline().split() # ex)push 0
    if cmd[0] == "push":
        stack.append(int(cmd[1]))

    if cmd[0] == "pop":
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()

    if cmd[0] == "size":
        print(len(stack))

    if cmd[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    if cmd[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])






