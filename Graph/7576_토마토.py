from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(box, ripen, n, m):
    q = deque(ripen)

    while q:
        cx, cy, cd = q.popleft()
        for i in range(4):
            nx, ny, nd = cx + dx[i], cy + dy[i], cd + 1
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == -1:
                    box[nx][ny] = nd
                    q.append((nx, ny, nd))


def solution(m, n, tomatos):
    ripen = []
    for i in range(n):
        for j in range(m):
            if tomatos[i][j] == 1:
                ripen.append((i, j, 0))
            tomatos[i][j] -= 1

    if len(ripen) == n * m:
        return 0

    bfs(tomatos, ripen, n, m)

    day = 0
    for i in range(n):
        if -1 in tomatos[i]:
            return -1
        day = max(day, max(tomatos[i]))
    return day


if __name__ == '__main__':
    n, m = map(int, input().split())
    tomatos = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, tomatos))
