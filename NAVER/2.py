from collections import deque


def solution(blocks):
    dic = dict()
    for i in range(len(blocks)):
        for j in range(i + 1):
            dic[(i, j)] = 0
        dic[(i, blocks[i][0])] = blocks[i][1]

    idx = 1
    for i in range(len(blocks)):
        q = deque(list(dic.keys())[idx - i - 1: idx])
        print(q)
        while q:
            x, y = q.popleft()
            if dic[(x, y)] == 0:
                if y - 1 >= 0 and dic[(x, y - 1)]\
                        != 0:
                    dic[(x, y)] = dic[(x - 1, y - 1)] - dic[(x, y - 1)]
                elif y + 1 <= i and dic[(x, y + 1)] != 0:
                    dic[(x, y)] = dic[(x - 1, y)] - dic[(x, y + 1)]
                else:
                    q.append((x, y))

        idx += i + 2

    return list(dic.values())


print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
