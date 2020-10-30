from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    on_weight = 0
    while queue:
        time += 1
        on_weight -= queue[0]
        queue.popleft()
        if trucks:
            if on_weight + trucks[0] <= weight:
                on_weight += trucks[0]
                queue.append(trucks.popleft())
            else:
                queue.append(0)

    return time


solution(2, 10, [7, 4, 5, 6])
