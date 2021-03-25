from collections import deque
mx, my = [-1, 0, 1, 0], [0, 1, 0, -1]
rx, ry = []


def move(x1, y1, x2, y2, i):
    nx1, ny1 = x1 + mx[i], y1 + my[i]
    nx2, ny2 = x2 + mx[i], y2 + my[i]
    return nx1, ny1, nx2, ny2


def rotate(x1, y1, x2, y2, i):



def avail_move_rotate(x1, y1, x2, y2, i, board):
    if i < 4 and any([board[x1][y1], board[x2][y2]]):
        return False
    if i

def avail_range(x1, y1, x2, y2, n):
    if not 0 <= x1 < n or not 0 <= y1 < n:
        return False
    if not 0 <= x2 < n or not 0 <= y2 < n:
        return False
    return True


def bfs(x1, y1, x2, y2, t, n):
    q = deque([(x1, y1, x2, y2, t)])
    visited = {(x1, y1, x2, y2)}

    while q:
        cx1, cy1, cx2, cy2, ct = q.popleft()
        if cx1 == n - 1 and cy1 == n - 1:
            return ct
        elif cx2 == n - 1 and cy2 == n - 1:
            return ct

        for i in range(12):
            if i < 4:
                nx1, ny1, nx2, ny2 = move(cx1, cy1, cx2, cy2, i)
            else:


            if not avail_range(nx1, ny1, nx2, ny2, n):
                continue
            if (nx1, ny1, nx2, ny2) in visited:
                continue

            q.append((nx1, ny1, nx2, ny2, ct + 1))
            visited.add((nx1, ny1, nx2, ny2))


def solution(board):
    n = len(board)
    return bfs(0, 0, 0, 1, 0, n)


print(solution([[0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]]))
