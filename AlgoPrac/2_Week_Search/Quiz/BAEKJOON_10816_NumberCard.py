from sys import stdin
from collections import Counter

N = int(stdin.readline())

answer = list(map(int, stdin.readline().split()))

M = int(stdin.readline())

mine = list(map(int, stdin.readline().split()))
'''
count = Counter(answer)

for i in range(len(mine)):
    c = mine[i]
    d = ' '.join(str((count[c])))
    print(int(d), end=" ")

이렇게하니깐 런타임 에러가 나왔다.
'''

# for의 사용을 최소화 해야한다.
count = Counter(answer)
print(' '.join(str(count[mine]) if mine in count else '0' for mine in mine))

# Practice
# count = Counter(a)
# c = (' '.join(count[b] if b in count else '0' for b in b))
# print(c)

