import sys
from collections import deque


N = int(sys.stdin.readline())
queue = deque([])





for i in range(N):
    cmd = sys.stdin.readline().split()
    # push X  : 정수 X를 큐에 넣는 연산이다.
    if cmd[0] == "push":
        queue.append(int(cmd[1]))

    # pop : 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력, 만약 큐에 들어있는 정수가 없는 경우 -1 출력
    if cmd[0] == "pop":
        if not queue:
            print('-1')
        else:
            print(queue.popleft())

    # size : 큐에 들어있는 정수의 개수를 출력한다.
    if cmd[0] == "size":
        print(len(queue))

    # empty : 큐가 비어있으면 1, 아니면 0
    if cmd[0] == "empty":
        if not queue:
            print('1')
        else:
            print(0)

    # front : 큐의 가장 앞에있는 정수 출력
    if cmd[0] == "front":
        if not queue:
            print('-1')
        else:
            print(queue[0])

    # 큐의 가장 뒤에 있는 정수를 출력
    if cmd[0] =="back":
        if not queue:
            print('-1')
        else:
            print(queue[-1])



