from collections import deque


def solution(enter, leave):
    n = len(enter)
    meet = [set() for _ in range(n + 1)]
    enter, leave = deque(enter), deque(leave)

    i, j = 0, 0
    while i < n or j < n:
        if enter[i] == 0:
            i += 1
        elif enter[i] != leave[j]:
            if enter[i] != 0 and enter[i + 1] != 0:
                meet[enter[i]].add(enter[i + 1])
                meet[enter[i + 1]].add(enter[i])
            i = min(i + 1, 3)
        else:
            for k in range(i):
                if enter[k] != 0:
                    meet[enter[k]].add(enter[i])
                    meet[enter[i]].add(enter[k])
            enter[i] = 0
            i = 0
            j += 1

    ans = []
    for m in meet[1:]:
        ans.append(len(m))

    return ans


print(solution([1, 4, 2, 3],
               [2, 1, 4, 3]))
