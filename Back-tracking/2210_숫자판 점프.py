import sys
readline = lambda: sys.stdin.readline().strip()


def dfs(cur_x, cur_y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    for k in range(4):
        next_x = cur_x + x[k]
        next_y = cur_y + y[k]
        if 0 <= next_x < 5 and 0 <= next_y < 5:
            dfs(next_x, next_y, number + matrix[next_x][next_y])


matrix = [list(map(str, input().split())) for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])
print(len(result))
