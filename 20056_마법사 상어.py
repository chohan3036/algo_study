# ball = (r, c, m, d, s) (x, y, 질량, 방향, 속도)
# 1번 행과 n번 행이 이어져 있고, 1번 열과 n번 열이 이어져 있음
# 원형 큐처럼 이어져 있는 모양... 걍 워프한다고 생각해
import sys
from collections import deque

read = lambda: sys.stdin.readline().strip()
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]


class FireBall:
    def __init__(self, m, s, d):
        self.m = m
        self.s = s
        self.d = d


def move(x, y):
    while board[(x, y)]:
        fire_ball = board[(x, y)].popleft()
        # 이동한 좌표 : 음수 나머지도 원하는 결과 나옴
        nx = (x + dx[fire_ball.d] * fire_ball.s) % n
        ny = (y + dy[fire_ball.d] * fire_ball.s) % n

        if (nx, ny) not in moved:
            moved[(nx, ny)] = deque([])
        moved[(nx, ny)].append(fire_ball)


def combine_and_split(x, y):
    nm, ns, nd = 0, 0, 0
    cnt = 0

    while board[(x, y)]:
        fire_ball = board[(x, y)].popleft()
        nm += fire_ball.m
        ns += fire_ball.s
        nd += fire_ball.d % 2
        cnt += 1

    nm = int(nm / 5)
    ns = int(ns / cnt)
    if nd == 0 or nd == 4:
        dirs = [0, 2, 4, 6]
    else:
        dirs = [1, 3, 5, 7]

    if nm > 0:
        for num in range(4):
            board[pos].append(FireBall(nm, ns, dirs[num]))


n, m, k = map(int, read().split())
board = dict()
for _ in range(m):
    r, c, m, s, d = map(int, read().split())
    r -= 1
    c -= 1
    if (r, c) not in board:
        board[(r, c)] = deque([])
    board[(r, c)].append(FireBall(m, s, d))

for _ in range(k):
    # 1. 모든 파이어볼 이동
    moved = dict()
    for pos in board:
        i, j = pos
        move(i, j)
    board.update(moved)

    # 2. 파이어볼이 겹쳤을 때
    will_remove = []
    for pos in board:
        if len(board[pos]) > 1:
            i, j = pos
            combine_and_split(i, j)
        if len(board[pos]) == 0:
            will_remove.append(pos)

    for key in will_remove:
        board.pop(key)

ans = 0
for pos in board:
    for fire_ball in board[pos]:
        ans += fire_ball.m

print(ans)
