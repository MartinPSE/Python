# 처음에 각각의 자릿수를 더하는거 까지는 무난히 생각했다.
# 그 후 처음 100을 채운놈이 나가는거까지 생각하면
# FIFO 즉 QUEUE를 사용해야함을 유추했다.
# 구현과정에서 조금 고생했지만.

from collections import deque


def solution(progresses, speeds):
    answer =[]
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        if count > 0:
            answer.append(count)
    return answer

print(solution([93, 30, 55],[1, 30 , 5]))

