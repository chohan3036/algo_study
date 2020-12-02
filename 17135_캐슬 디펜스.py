import sys
read = lambda: sys.stdin.readline().strip()
from itertools import combinations


def enemy_move():
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if field[i][j]:
                field[i][j] -= 1
                field[i + 1][j] += 1


def dist_to_enemy():



n, m, d = map(int, read().split())
field = [list(map(int, read().split())) for _ in range(n)]
archer_pos = combinations([i for i in range(m)], 3)

