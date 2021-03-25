''' 함수가 거의 비슷한 모양, 낭비 심함
def balanced(w):
    flag = 0
    for i in range(len(w)):
        if w[i] == '(':
            flag += 1
        else:
            flag -= 1

        if flag == 0:
            return w[: i + 1], w[i + 1:]


def is_right(u):
    flag = 0
    for i in range(len(u)):
        if u[i] == '(':
            flag += 1
        else:
            flag -= 1

        if flag < 0:
            return False
    return True
'''


def flip(u):
    flipped = map(lambda x: '(' if x == ')' else ')', u[1: -1])
    return ''.join(flipped)


def solution(string):
    ans = ''

    # 1
    if not string:
        return ''

    w = string
    balance = 0
    flag = True
    for i in range(len(w)):
        # 2 + 3
        if w[i] == '(':
            balance += 1
        else:
            balance -= 1

        # 올바른 괄호인가?
        # (균형잡힌 괄호 찾기 전에 확인할 수 있음)
        if balance < 0:
            flag = False

        # 균형잡힌 괄호 찾으면
        # u의 균형 여부에 따라 진행
        if balance == 0:
            u, v = w[: i + 1], w[i + 1:]
            if flag:
                return u + solution(v)
            else:
                return ans + '(' + solution(v) + ')' + flip(u)


print(solution(")("))
