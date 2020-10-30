from itertools import permutations
from collections import deque

OPERATOR = {'+', '-', '*'}


def solution(expression):
    # 연산자와 피연산자 단위로 잘라 큐에 넣음
    num = ''
    queue = []
    op = set()
    for x in expression:
        if x in OPERATOR:
            op.add(x)
            queue.append(num)
            queue.append(x)
            num = ''
        else:
            num += x
    queue.append(num)   # 마지막 거 넣어주기

    # 케이스에 나온 연산자만 이용해 순열 만들기(순열의 인덱스 순서 = 우선순위)
    cases = list(permutations(op, len(op)))

    ans = 0
    # 각 순열을 순회하며
    for c in cases:
        # 큐와 스택을 생성
        q = deque(queue)
        stack = deque([])
        # 이번 순열의 우선순위대로 큐를 순회하며 계산
        for cop in c:
            while q:
                now = q.popleft()
                # 현재 우선순위에 해당하는 연산자면
                if now == cop:
                    # 스택 맨 뒤, 큐 맨 앞 피연산자 뽑아오기
                    opd1 = stack.pop()
                    opd2 = q.popleft()
                    stt = opd1 + cop + opd2
                    # 피연산자1, 연산자, 피연산자2 세 개를 하나의 문자열로 만들어 eval 계산
                    stack.append(str(eval(stt)))
                else:
                    # 그 이외에는 스택에 쌓아줌
                    stack.append(now)

            # 이번 우선순위에 해당하는 계산 끝나면 스택을 다시 큐로 넣어줌
            q.extend(stack)
            stack.clear()

        # 순열 하나 볼 때마다 ans 갱신(음수는 절댓값으로)
        ans = max(ans, abs(int(q.pop())))
    return ans


print(solution("100-200*300-500+20"))
