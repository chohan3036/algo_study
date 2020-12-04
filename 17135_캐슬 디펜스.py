import sys
read = lambda: sys.stdin.readline().strip()
from itertools import combinations
from copy import deepcopy

#n, m, d = map(int, read().split())
#field = [list(map(int, read().split())) for _ in range(n)]
n, m, d = 5, 5, 5
field = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]

enemies = []
for i in range(n):
    for j in range(m):
        if field[i][j]:
            enemies.append([i, j])


max_shot = 0
archer_combi = combinations([i for i in range(m)], 3)
for archers in archer_combi:
    cur_field = deepcopy(field)
    cur_enemies = deepcopy(enemies)
    cur_shot = 0
    while cur_enemies:
        will_shot = []
        for archer in archers:
            min_dist = d
            target = [n, m]
            for enemy in cur_enemies:
                dist = abs(n - enemy[0]) + abs(archer - enemy[1])
                if min_dist > dist or (min_dist == dist and target[1] > enemy[1]):
                    min_dist = dist
                    target = enemy
            if not target == [n, m] and target not in will_shot:
                will_shot.append(target)

        for x, y in will_shot:
            cur_field[x][y] = 0
            cur_shot += 1
            cur_enemies.remove([x, y])

        for i in range(len(cur_enemies) - 1, -1, -1):
            if cur_enemies[i][0] == n - 1:
                cur_enemies.pop()
            else:
                cur_enemies[i][0] += 1

    max_shot = max(max_shot, cur_shot)

print(max_shot)