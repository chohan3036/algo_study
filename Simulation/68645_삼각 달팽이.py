def solution(n):
    snail = [[0] * i for i in range(1, n + 1)]
    dir_list = [(1, 0), (0, 1), (-1, -1)]
    dest = (n + 1) * n // 2
    cur_num = 1
    i, j = 0, 0
    step, step_cnt, dir, = n, 1, 0
    while cur_num <= dest:
        snail[i][j] = cur_num

        if step > 0:
            step -= 1

        if step == 0:
            dir = (dir + 1) % 3
            step = n - step_cnt
            step_cnt += 1

        i, j = i + dir_list[dir][0], j + dir_list[dir][1]
        cur_num += 1

    return sum(snail, [])


print(solution(5))
