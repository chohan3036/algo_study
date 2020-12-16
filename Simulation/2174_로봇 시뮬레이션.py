import sys

read = lambda: sys.stdin.readline().strip()
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
dirs = ['N', 'E', 'S', 'W']

a, b = map(int, read().split())
board = [[0 for _ in range(a)] for _ in range(b)]

n, m = map(int, read().split())
robots, commands = [], []
for _ in range(n):
    x, y, r_dir = map(str, read().split())
    x, y = int(y) - 1, int(x) - 1
    robots.append([x, y, r_dir])
    board[x][y] = 1

for _ in range(m):
    r_idx, comm, rp = map(str, read().split())
    r_idx, rp = int(r_idx) - 1, int(rp)
    commands.append((r_idx, comm, rp))


def do_command(i, c, r):
    if c == 'L':
        robots[i][2] = dirs.index(robots[i][2]) - (r % 4)

    elif c == 'R':
        robots[i][2] = dirs.index(robots[i][2] + (r % 4))

    else:
        cx, cy = robots[i][0], robots[i][1]
        nx, ny = cx + int(dx[dirs.index(robots[i][2])]) * r, cy + int(dy[dirs.index(robots[i][2])]) * r




failed = False
for command in commands:
    r_idx, comm, rp = command
    result = do_command(r_idx, comm, rp)
    if not result:
        print('Robot ', r_idx + 1, ' crashes into the wall')
        failed = True
        break

if not failed:
    print('OK')
