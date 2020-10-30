dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def find_block(map):
    pop_block = set()

    for i in range(len(map) - 1):
        for j in range(len(map[i]) - 1):
            if j >= len(map[i + 1]) - 1:
                continue
            if map[i][j] == map[i][j + 1] == map[i + 1][j] == map[i + 1][j + 1]:
                for x, y in zip(dx, dy):
                    pop_block.add((i + x, j + y))

    return pop_block


m, n = 6, 6
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

num_poped_blocks = 0
tilted_board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
while 1:
    pop_list = find_block(tilted_board)
    if not pop_list:
        break
    for x, y in reversed(sorted(pop_list)):
        tilted_board[x].pop(y)
        num_poped_blocks += 1
    pop_list.clear()
