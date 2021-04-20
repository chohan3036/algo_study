from collections import deque


def bfs(start):
    q = deque([start])

    cnt = [-1] * f
    cnt[start] = 0

    while q:
        cur_floor = q.popleft()

        if cur_floor == g - 1:
            return cnt[cur_floor]

        for i in range(2):
            if i == 0:
                next_floor = cur_floor + u
            else:
                next_floor = cur_floor - d

            if not 0 <= next_floor < f or cnt[next_floor] != -1:
                continue

            q.append(next_floor)
            cnt[next_floor] = cnt[cur_floor] + 1

    return 'use the stairs'


f, s, g, u, d = map(int, input().split())
print(bfs(s - 1))
