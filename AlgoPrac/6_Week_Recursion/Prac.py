# 올바른 괄호(?)
def correct(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return False
    return True


# 균형잡힌 괄호

def balance(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        else:
            count -= 1

    if count == 0:
        return True
    else:
        return False


# STEP 4에서 쓰일 용도의 전환
def convert(s):
    source = ''
    for i in s:
        if i == "(":
            source += ")"
        else:
            source += "("
    return source


# 4 단계 로직을 실행

def answer(s):
    u = ''  # 무조건 균형잡힌 문자열의 최소단위
    v = ''  # u 빼고 나머지
    result = ''  # 결과

    # 1
    if correct(s):  # 올바른 문자열이면 끝내면 됨, 혹은 공백
        return s

    # 2 분리해야해
    for i in range(2,len(s)+1):
        if balance(s[:i]):
            u = s[:i]
            v = s[i:]
            break
    # 3단계
    if correct(u):
        result = u + answer(v)

    # 4단계

    else:
        result = ''
        result += '('
        result += answer(v)
        result += ')'
        result += convert(u[1:-1])

    return result


'''
엄청난 풀이다.. 

def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


'''