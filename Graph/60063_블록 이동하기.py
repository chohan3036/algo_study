from collections import deque
turn = [(1, -1), (-1, -1), (1, 1), (-1, 1)]


def bfs(x1, y1, x2, y2, depth, mat):
    q = deque([(x1, y1, x2, y2, depth)])
    visited = set()
    visited.add((x1, y1, x2, y2))

    while q:
        px1, py1, px2, py2, plv = q.popleft()
        # 두 축에 대해 두 방향으로 회전이 가능
        for i in range(4):
            # 축이 왼/아래 일 때
            if i in (0, 1):
                nx1, ny1 = px1, py1
                nx2, ny2 = px2 + turn[i][0], py2 + turn[i][1]
            # 축이 오/위 일 때
            else:
                nx1, ny1 = px1 + turn[i][0], py1 + turn[i][1]
                nx2, ny2 = px2, py2

            # 아래쪽으로 회전하는 경우
            if i == 0:
                if mat[px2][]

            if (nx1, ny1, nx2, ny2) not in visited:
                q.append((nx1, ny1, nx2, ny2, depth + 1))
                visited.add((nx1, ny1, nx2, ny2))

     return depth

def solution(board):
    return bfs(0, 0, 0, 1, 0, board)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],[1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]]))
