from collections import deque
# 없앨 수 있는 경우만 리스트에 저장
# 직사각형도 고려해야 돼
possible = [{(0, 0), (1, -1), (1, 0), (1, 1)},      # ㅗ
            {(0, 0), (1, -2), (1, -1), (1, 0)},     # ┘
            {(0, 0), (1, 0), (1, 1), (1, 2)},       # ㄴ
            {(0, 0), (1, 0), (2, 0), (2, 1)},       # ㄴ
            {(0, 0), (1, 0), (2, -1), (2, 0)}]      # ┘
recangle = [[(0, -1), (0, 1)],
            [(0, -2), (0, -1)],
            [(0, 1), (0, 2)],
            [(1, 1)],
            [(1, -1)]]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(x, y, block, board):
    q = deque([(x, y)])
    visit = {(x - x, y - y)}

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not 0 <= nx < len(board) or not 0 <= ny < len(board[0]):
                continue
            if (nx - x, ny - y) in visit:
                continue
            if board[nx][ny] != block:
                continue

            q.append((nx, ny))
            visit.add((nx - x, ny - y))

            if len(visit) >= 4:
                return visit


def upper_chk(x, y, board):
    for i in range(x, -1, -1):
        if board[i][y] != 0:
            return False
    return True


def solution(board):
    ans = 0
    block_num = [0]
    for i in range(len(board)):
        if not any(board[i]):
            continue

        for j in range(len(board[0])):
            if board[i][j] not in block_num:
                block = bfs(i, j, board[i][j], board)
                if block in possible:
                    flag = True
                    rec_idx = possible.index(block)
                    for x, y in recangle[rec_idx]:
                        if not upper_chk(x + i, y + j, board):
                            flag = False
                            break
                    if not flag:
                        continue

                    for k in range(4):
                        x, y = block.pop()
                        board[x + i][y + j] = 0
                    ans += 1
                else:
                    block_num.append(board[i][j])

    return ans


print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
