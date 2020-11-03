from collections import deque


def solution(n, edges):
    ans = 0
    parent, lv = dict(), dict()
    depth = 0
    for i in range(len(edges) - 1, -1, -1):
        # 자식 노드 수 더해주기
        p, c = edges[i][0], edges[i][1]
        if p not in parent:
            parent[p] = 1
        else:
            parent[p] += 1
        if c in parent:
            parent[p] += parent[c]

        # 각 레벨 저장하기
        if p not in lv:
            lv[depth] = {c}
        else:
            if c not in lv:
                lv[depth].add(c)
            else:
                depth += 1
                lv[depth].add(c)

    print(lv)
    #order = deque(sorted(parent.items(), key=lambda x: (-x[1], x[0]))[1: ])
    #while order:
    #    coms = order.popleft()
    #    ans += coms

    return ans

print(solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
