from collections import deque


def solution(N, simulation_data):
    waiting = []
    total_wait_time = 0
    wait_time = 0
    queue = deque(simulation_data)
    csl = []
    while queue:
        if len(csl) < N:
            if queue[0][0] == total_wait_time or queue[0][0] > total_wait_time:
                csl.append(queue.popleft())
        # 창구가 다 찼다
        else:
            for q in queue:
                if q[0] <= total_wait_time:
                    wait_time += 1

        for c in csl:
            c[1] -= 1
            if c[1] == 0:
                csl.remove(c)

        total_wait_time += 1
    return wait_time


print(solution(1, [[2, 3], [5, 4], [6, 3], [7, 4]]))
