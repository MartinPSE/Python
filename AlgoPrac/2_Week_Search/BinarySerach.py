# 이진검색이라고도 하며, 오름차순으로 '정렬된 리스트' 에서 특정 값의 위치를 찾는 알고리즘
# '중간의 값'을 선택하여 찾고자 하는 값과의 크고 작음을 비교 하는 방법

'''

def solution(trump):
    left = 0  index 설정
    right = len(trump-1)  # index 설정
    while(left <= right):  # 범위 ~~
        mid = ( left + right ) // 2  # 우리의 주인공 mid
        if trump[mid] == 8 :
            return mid
        elif trump[mid] < 8:
            left = mid + 1
        elif trump[mid] > 8:
            right = mid - 1
    return mid

'''
