'''
 < Stack >
  LIFO - Last In First Out
  1. Push --> LIST 맨위에 추가
  2. Pick --> '엿보다'  맨 마지막 데이터 보자
  3. Pop ---> 맨 마지막 데이터 빼자

'''


class Stack(list):
    push = list.append

    def peek(self):
        return self[-1]  # peek

        # pop 은 미리 있어.


s = Stack()
s.push(1)
s.push(5)
s.push(10)
print(s)
print("popped value is : ", s.pop())
print('my stack is ', s)
print("peeked value is", s.peek())
print('my stack is ', s)

s = []
s.append(1)
s.append(5)
s.append(10)
print("my stack is ", s)
print("popped value is  : ", s.pop())
print('my stack is ', s)
print("peeked value is : ", s[-1])
print('my stack is ', s)

'''
 # 스택의 활용
 1. 이전 페이지/ 다음 페이지 

'''
