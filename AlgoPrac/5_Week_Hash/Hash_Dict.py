# 딕셔너리 = Hash
# 집합과 배열은 key값으로 사용 불가

hash = dict()  # hash = {}
hash[1] = 'apple'
hash['banana'] = 3
hash[(4, 5)] = [1, 2, 3]  # tuple 은 가능

hash[10] = dict({1: 'a', 2: 'b'})

# pop 사용
hash[1] = 'melon'

print(hash.pop("banana"))

# del 함수 // 지워버리는거
del hash[1]
print(hash)

# 딕셔너리 루프 // 딕셔너리 정렬
'''
딕셔너리 loop
1 . key값? ---> .keys()
2.  value 값? ---> .values()
3 . key,value값? ----> .items()

'''

print(hash.keys())  # key를 list와 유사한 형태로 추출
print(hash.values())  # value를 list와 유사한 형태로 추출
print(hash.items())  # key와 value를 list와 유사한 형태로 추출

hash = dict()

for i in range(1, 6):
    hash[i] = i ** 2

for k in hash.keys():
    print(k)

for k in hash.values():
    print(k)

for k, v in hash.items():
    print(k, v)

'''
딕셔너리 정렬
1. sorted() ---> 언제나 list를 반환
# 오름차순 : lambda 함수를 이용하여(key를)
sorted( hash.keys(), key = lambda x : x)
value를.
sorted( hash.values(), key = lambda x : x)
key와 value 모두
print(sorted( hash.items(), key = lambda x : x))

# 내림차순 
sorted( hash.keys(), key = lambda x : -x)
// tuple에는 -를 줄 수 없어서 
sorted( hash.values(), key = lambda x : -x[1])
//
 x[0] , x[1] -- key 오름차순 value 오름차순
-x[0] , x[1] -- key 내림차순, value 오름차순
 x[1] , x[0] -- value,key 내림차순

sorted( hash.items(), key = lambda x : -x[1])

'''

# 오름차순 정렬
print(sorted(hash.keys(), key=lambda x: x))
print(sorted(hash.values(), key=lambda x: x))
print(sorted(hash.items(), key=lambda x: x))

print(sorted(hash.values(), key = lambda x : x[0]))