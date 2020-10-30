def slicing(string):
    left, right = 0, 0
    u, v = '', ''
    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = string[0: i + 1]
            v = string[i + 1:]
            break
    return u, v


def is_right(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return False if stack else True


def solution(string):
    answer = ''
    # 빈 문자열이거나 전체가 올바른 괄호 문자열이면 그대로 반환
    if string == '' or is_right(string):
        return string

    # 문자열을 균형 잡힌 괄호 문자열로 분리
    u, v = slicing(string)

    # u가 올바른 괄호 문자열이라면
    if is_right(u):
        next_v = solution(v)
        return u + next_v

    # u가 올바른 괄호 문자열이 아닌 경우
    else:
        # 첫번째 (
        answer += '('
        # 두번째 v를 재귀적으로 실행한 결과
        answer += solution(v)
        # 세번째 )
        answer += ')'
        # 네번째 u의 앞뒷문자 제거
        u = u[1:-1]
        # u는 균형잡힌 문자열임으로 길이의 반만큼 rotate하면 반전됨
        # 위처럼 하니까 틀림.. 하나씩 바꾸어줌
        new_u = ''
        for i in range(len(u)):
            if u[i] == '(':
                new_u += ')'
            else:
                new_u += '('
        answer += new_u
        return answer


p = '()))((())'
print(solution(p))
