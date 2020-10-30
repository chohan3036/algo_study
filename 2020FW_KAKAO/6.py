from collections import deque


def command(n):
    if n == 0:
        pass


def bfs(x, y, mat, depth):
    # 보드가 모두 뒤집어질 때까지 조작
    # 조작횟수가 늘어날 때마다 depth + 1
    q = deque([(x, y, depth)])


def solution(board, r, c):
    bfs(r, c, board, 0)
    answer = 0
    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
