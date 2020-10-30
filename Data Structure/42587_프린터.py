from collections import deque


def solution(priorities, location):
    q = deque(enumerate(priorities))
    order = 0
    while q:
        _max = 0
        idx = 0
        for i in range(len(q)):
            if _max < q[i][1]:
                _max = q[i][1]
                idx = i

        q.rotate(-idx)
        escape = q.popleft()
        order += 1
        if escape[0] == location:
            return order


print(solution([2, 1, 3, 2], 2))
