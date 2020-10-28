def quad_check(x, y, size, arr, ans):
    cur_num = arr[x][y]

    break_flag = False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != cur_num:
                break_flag = True
                break
        if break_flag:
            break

    if not break_flag:
        ans[cur_num] += 1

    else:
        quad_check(x, y, size // 2, arr, ans)
        quad_check(x, y + size // 2, size // 2, arr, ans)
        quad_check(x + size // 2, y, size // 2, arr, ans)
        quad_check(x + size // 2, y + size // 2, size // 2, arr, ans)


def solution(arr):
    ans = [0, 0]
    quad_check(0, 0, len(arr), arr, ans)
    return ans


print(solution([[1,1,0,0],
                [1,0,0,0],
                [1,0,0,1],
                [1,1,1,1]]))
