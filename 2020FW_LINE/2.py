from collections import deque


def solution(ball, order):
    ans = []
    # popleft 를 사용하기 위해 deque 로 전환
    ball = deque(ball)
    order = deque(order)
    wait = deque([])
    # order 를 순회하며 공을 뺌
    while order:
        cur_order = order.popleft()

        # 빼길 원하는 공이 파이프 양끝에 있으면
        # 공을 빼고 ans 에 추가
        if cur_order == ball[0]:
            ans.append(ball.popleft())
        elif cur_order == ball[-1]:
            ans.append(ball.pop())

        # 그렇지 않으면 보류하기 위해 바로 다음 인덱스에 삽입
        else:
            wait.append(cur_order)

        print(order, wait)
    return ans


print(solution([11, 2, 9, 13, 24], 	[9, 2, 13, 24, 11]))
