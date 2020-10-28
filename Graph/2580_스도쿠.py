import sys
read = lambda: sys.stdin.readline().strip()

area = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def chk(i, j):
    # 가로
    if board[i][j] in (board[i][: j] or board[i][j + 1:]):
        return False

    # 세로
    tp = [x for x in zip(*board)]
    if tp[j][i] in (tp[j][: i] or tp[j][i + 1:]):
        return False

    # 정사각형
    smaller_board = []
    for x in range(3):
        for y in range(3):

    if board[i][j] in smaller_board:
        return False


def btk():
    if not blank:
        return



#board = [[list(map(int, read()))] for _ in range(9)]
board = [[0, 3, 5, 4, 6, 9, 2, 7, 8],
         [7, 8, 2, 1, 0, 5, 6, 0, 9],
         [0, 6, 0, 2, 7, 8, 1, 3, 5],
         [3, 2, 1, 0, 4, 6, 8, 9, 7],
         [8, 0, 4, 9, 1, 3, 5, 0, 6],
         [5, 9, 6, 8, 2, 0, 4, 1, 3],
         [9, 1, 7, 6, 5, 2, 0, 8, 0],
         [6, 0, 3, 7, 0, 1, 9, 5, 2],
         [2, 5, 8, 3, 9, 4, 7, 6, 0]]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

