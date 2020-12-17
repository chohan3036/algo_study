import sys


def far(x, y, positions):
    dist = 0
    for position in positions:
        dist += abs(position[0] - x) + abs(position[1] - y)
    return dist


def solution(positions):
    r = c = 0
    for position in positions:
        x, y = position
        if abs(r) < abs(x):
            r = abs(x)
        if abs(c) < abs(y):
            c = abs(y)

    min_dist = sys.maxsize
    locate = []
    locate_x = [i for i in range(-r, r + 1)]
    locate_y = [i for i in range(-c, c + 1)]
    for i in locate_x:
        for j in locate_y:
            cur_dist = far(i, j, positions)
            if min_dist >= cur_dist:
                min_dist = cur_dist
                locate.append((i, j, cur_dist))

    ans = []
    for lo in locate:
        if lo[2] == min_dist:
            ans.append((lo[0], lo[1]))

    return ans


print(solution([[1, 1], [-1, -1], [-1, 1], [0, 0]]))
