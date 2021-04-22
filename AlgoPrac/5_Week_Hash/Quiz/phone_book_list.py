# 접두어에 포함 된 경우 false
# 접두어에 포함 안된 경우 true

# 이번에도 그냥 가볍게 생각하면 아예 안겹치는 놈들을 해결을 못한다.
# phone_book = ["119", "97674223", "1195524421"]
#
# answer = True
#
# for number in phone_book:
#     for i in range(len(phone_book)):
#         if number in phone_book[i]:
#             answer = False
#
# print(answer)

# 2
phone_book = ["119", "97674223", "1195524421"]
phone_book2 = ["123", "456", "789"]
phone_book3 = ["12","123","1235","567","88"]

def solution(phone_book):
    answer = True
    phone_book.sort() # 생명

    for x, y in zip(phone_book, phone_book[1:]):
        print("x",x,"y",y)
        if y.startswith(x):
            answer = False
            break
    return answer

    # 119 , 97674223
    #       97674223, 11955524421


print(solution(phone_book3))

# startswith 함수
'''
startswith(시작하는문자, 시작지점)
startswith(시작하는문자) return True | False

'''


# 해쉬를 쓴 풀이
# 풀이를 참조했다.
def solution2(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1  # value는 임의로~

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer


