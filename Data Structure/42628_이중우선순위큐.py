import heapq


def solution(operations):
    h = []

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == 'I':
            heapq.heappush(h, num)
        else:
            if h:
                if num == 1:
                    h.pop(h.index(heapq.nlargest(1, h)[0]))
                else:
                    heapq.heappop(h)

    if not h:
        return [0, 0]
    else:
        return [max(h), min(h)]


print(solution(['I 1', 'I 2', 'I 3', 'I 4', 'I 5',
                'I 6', 'I 7', 'I 8', 'I 9', 'I 10',
                'D 1', 'D -1', 'D 1', 'D -1',
                'I 1', 'I 2', 'I 1']))
