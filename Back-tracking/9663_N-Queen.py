def queen(x, y):
    for i in range(n):
        k = abs(x - i)
        # 대각선 검사
        if k > 0:
            if (y - k >= 0 and board[i][y - k]) or (y + k < n and board[i][y + k]):
                return False
        # 가로 검사
        else:
            if sum(board[i]) > 1:
                return False
        # 세로 검사
        if i != x and board[i][y]:
            return False
    return True


def dfs(cnt, chess):
    global ans, ans_board
    # 탈출 조건
    if cnt == 0:
        tmp = sorted(chess)
        if tmp not in ans_board:
            ans += 1
            ans_board.append(tmp)
        return

    # 진행
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and (i, j) not in chess:
                board[i][j] = 1
                if queen(i, j):
                    chess.append((i, j))
                    dfs(cnt - 1, chess)
                    chess.pop()
                board[i][j] = 0


n = int(input())
board = [[0] * n for _ in range(n)]

ans = 0
ans_board = []

dfs(n, [])

print(ans)
