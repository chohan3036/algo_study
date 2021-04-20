# deque rotation이나 base를 배열로 만들어서 하는 것도 시간초과 남..
# 그럼 직접 돌려야지..

from itertools import permutations
import sys
read = lambda: sys.stdin.readline().strip()

n = int(read())
innings = [list(map(int, read().split())) for _ in range(n)]
ans = 0


def play(batters):
    score = 0
    idx = -1
    for inning in innings:
        out_cnt = 3
        b1, b2, b3 = 0, 0, 0
        while out_cnt > 0:
            idx = (idx + 1) % 9
            # cur_bat = inning[batters[idx]]
            if inning[batters[idx]] == 0:
                out_cnt -= 1
            elif inning[batters[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[batters[idx]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inning[batters[idx]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0

    return score


orders = permutations([i for i in range(1, 9)], 8)
for order in orders:
    order = list(order)
    batters = order[:3] + [0] + order[3:]
    score = play(batters)
    if ans < score:
        ans = score

print(ans)
