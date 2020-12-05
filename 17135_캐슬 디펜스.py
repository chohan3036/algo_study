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
    # 조합마다 필드, 적, 죽인 횟수를 각각 구해줄 것임
    # 깊은 복사 해줌
    cur_field, cur_enemies, cur_shot = deepcopy(field), deepcopy(enemies), 0

    # 적이 남아있는 동안 반복
    while cur_enemies:
        # 쏠 적들
        will_shot = []
        # 궁수들마다 가장 가까운 적을 찾아서 저장함
        for archer in archers:
            min_dist = d
            target = [n, m]
            for enemy in cur_enemies:
                # 맨하탄 거리
                dist = abs(n - enemy[0]) + abs(archer - enemy[1])
                # 거리가 더 작거나, 열이 더 적은 경우
                if min_dist > dist or (min_dist == dist and target[1] > enemy[1]):
                    min_dist = dist
                    target = enemy
            # 쏠 수 없는 적이 없는 경우에는 target이 그대로 n, m
            # 다른 궁수와 적이 겹친 경우
            if not target == [n, m] and target not in will_shot:
                will_shot.append(target)

        # 쏜 적들을 필드에서 지우기
        for x, y in will_shot:
            cur_field[x][y] = 0
            cur_shot += 1
            cur_enemies.remove([x, y])

        # 적들이 움직이면서 성에 가까이 가면 필드에서 제외시킴
        for i in range(len(cur_enemies) - 1, -1, -1):
            if cur_enemies[i][0] == n - 1:
                cur_enemies.pop()
            else:
                cur_enemies[i][0] += 1

    # 이번 조합에서 적을 쏜 횟수와 비교해 최댓값 갱신
    max_shot = max(max_shot, cur_shot)

print(max_shot)
