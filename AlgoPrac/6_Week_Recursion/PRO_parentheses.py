'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.

2. 문자열 w를 두 "균형잡힌 괄호 문자열(balance)" u, v로 분리합니다.
단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        ( balance )

3. 문자열 u가 "올바른 괄호 문자열(correct)" 이라면, 문자열 v에 대해 1단계부터 다시 수행합니다. ( v --> u1, v1 )
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        ( u + output(?) )

4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.


'''


# 1 올바른 문자열!
def correct(n):
    cnt = 0
    for s in n:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    return True


# 2 균형잡힌 문자열!
def balance(n):
    cnt = 0
    for s in n:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        return True
    else:
        return False


# 3 뒤집자! 나중에 더해져야하니깐
def convert(s):
    ans = ''
    for i in s:
        if i == '(':
            ans += ')'
        else:
            ans += '('

    return ans


def answer(s):
    u = ''
    v = ''
    result = ''

    if correct(s):  # 올바른 문자열 이거나 공백이면 끝내고
        return s

    for i in range(2, len(s) + 1):  # 균형잡힌 문자열을 찾자.
        if balance(s[:i]):  # 무조건 u 는 짝을이룬다. 즉, 최소한 0 1 번째까지. |ex| )(  ()   ))((  와 같이.
            u = s[:i]  # 균형잡힌문자열의 중복 없는 최초 놈을 u로 선택하고
            v = s[i:]  # 그 나머지는 v로 선택한다
            break

    if correct(u):  # 선택받은 u가 올바른 문자열이면 + v의 output 과 더한다.
        result = u + answer(v)


    else:  # Step 4를 실행한다. u != correct 인 경우.
        result = ''
        result += '('
        result += answer(v)
        result += ')'
        result += convert(u[1:-1])

    return result


string = "1234"
print(string[1:-1])