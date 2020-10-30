board = [[0] * 8 for _ in range(8)]
col = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
       'E': 4, 'F': 5, 'G': 6, 'H': 7}
move = {'LT': (1, -1), 'T': (1, 0), 'RT': (1, 1), 'R': (0, 1),
        'RB': (-1, 1), 'B': (-1, 0), 'LB': (-1, -1), 'L': (0, -1)}

king, stone, n = map(str, input().split())
king, stone = list(king), list(stone)
king[1], stone[1] = int(king[1]) - 1, int(stone[1]) - 1
n = int(n)

print(king)
print(stone)

board[king[1]][col[king[0]]] = 1
board[stone[1]][col[stone[0]]] = 2

for _ in range(n):
    dx, dy = move[input()]
    nx, ny = king[1] + dx, col[king[0]] + dy
    if not 0 <= nx < 8 or not 0 <= ny < 8:
        continue

    if board[nx][ny] == 0:
        king[1], king[0] = nx, ny
    elif board[nx][ny] == 2:
        if not 0 <= nx + dx < 8 or not 0 <= ny + dy < 8:
            continue
        stone[1], stone[0] = nx + dx, ny + dy
        king[1], king[0] = nx, ny

#print(''.join([king[0], str(king[1] + 1)]))
#print(''.join([stone[0], str(stone[1] + 1)]))
print(king)
print(stone)
