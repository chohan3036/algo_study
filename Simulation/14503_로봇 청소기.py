import sys
read = lambda: sys.stdin.readline().strip()


def search(i, j, cur_dir):
    global clean_cnt, turn_cnt
    while True:
        if turn_cnt == 4:
            if place[i - turn_x[cur_dir]][j - turn_y[cur_dir]] == 1:
                break
            else:
                turn_cnt = 0
                i = i - turn_x[cur_dir]
                j = j - turn_y[cur_dir]

        if place[i][j] == 0:
            place[i][j] = 2
            clean_cnt += 1

        left = dir[cur_dir - 1]

        if place[i + turn_x[left]][j + turn_y[left]] == 0:
            turn_cnt = 0
            i = i + turn_x[left]
            j = j + turn_y[left]
            cur_dir = left
        else:
            turn_cnt += 1
            cur_dir = left


N, M = map(int, read().split())
r, c, d = map(int, read().split())

dir = [0, 1, 2, 3]
turn_x = [-1, 0, 1, 0]
turn_y = [0, 1, 0, -1]

place = []
for _ in range(N):
    place.append(list(map(int, read().split())))

clean_cnt, turn_cnt = 0, 0
search(r, c, d)
print(clean_cnt)
