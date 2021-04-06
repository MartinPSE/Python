'''
 << Queue >>
 '일이 처리되기를 기다리는 리스트'

 FIFO -> First In Frist Out  즉, 선착순

'''


# 1. Put -- > List 맨 끝에 데이터 추가 --> append 사용
# 2. Peek --> 가장 먼저 들어간 데이터가 뭔지 확인! ( 확인만 !! )
# 3. Get -->  먼저 들어간 데이터를 가져오자. --> pop

# 1. 직접 구현

class Queue(list):
    put = list.append

    def peek(self):
        return self[0]

    def get(self):
        return self.pop(0)


q = Queue()
q.put(1)
q.put(5)
q.put(10)
print("My Queue is :", q)
print("Removed Value is :", q.get())
print("My queue is :",q)
print("Peeked value is ",q.peek())
print("My queue is :",q)

# 2 . python 구현된 클래스 import
from queue import Queue

q1 = Queue()
q1.put(1)
q1.put(5)
q1.put(10)
print("My Queue is :", q1)
print("Removed value is  : ", q1. get())
print("My Queue is :",q1)

# 3. list 를 Queue로 써보자
list = [];
list.append(1)
list.append(1)
list.append(1)
print(list)
print(list.pop(0))

# Queue 의 활용
# 프린트 인쇄 대기열
