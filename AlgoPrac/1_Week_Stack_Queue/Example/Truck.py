'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truck_weights = deque(truck_weights)

    while truck_weights: // 다리길이를 따라 갈 수가 없어.
        print(bridge, truck_weights, answer)

        for i in range(len(bridge)):
            bridge[-i] = truck_weights.popleft()
            answer += 1

            if sum(bridge) > weight: // 들어오고나서가 아니라 -> 들어오기전에 확인해야해!!
                bridge.pop(0)
                answer += 1

            else:
                answer += 1



    return answer
'''
## 초안. 1번째 테스트 통과 나머지 테스트는 실패
## 고민.. 또 고민..
## 시간이 너무 오래걸린다.

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truck_weights = deque(truck_weights)

    while bridge:  # 다리가 없어
        print(answer, bridge, truck_weights)
        answer += 1
        bridge.pop(0)  # 시작과 동시에 트럭이 들어오니 POP 해주자!
        if truck_weights:  # 트럭이 텅텅 빌때까지
            if sum(bridge) + truck_weights[0] <= weight:  # 무게를 넘지 않아야 하잖아.
                bridge.append(truck_weights.popleft())  # 안 넘으면 트럭을 다리로 보내고
            else:
                bridge.append(0)  # 넘으면 원래 있던 트럭을 전진.

    return answer


# bridge를 QUEUE 처럼 사용해서, 더 쉽게 생각해보기.

print(solution(2, 10, [7, 4, 5, 6]))
