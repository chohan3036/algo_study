# 좌표 집합을 만들고 순회하면서 바꾸자
inf = 100001


def turn(query, arr):
    query = [i - 1 for i in query]  # index 로 변환
    x1, y1, x2, y2 = query

    dots = []
    # hor1
    for i in range(y1 + 1, y2 + 1):
        dots.append((x1, i))
    # ver1
    for i in range(x1 + 1, x2 + 1):
        dots.append((i, y2))
    # hor2
    for i in range(y2 - 1, y1 - 1, -1):
        dots.append((x2, i))
    # ver2
    for i in range(x2 - 1, x1 - 1, -1):
        dots.append((i, y1))

    flag = arr[x1][y1]
    mini = inf
    for i in range(len(dots) - 1, 0, -1):
        x, y = dots[i]
        tx, ty = dots[i - 1]
        mini = min(mini, arr[x][y], arr[tx][ty])
        arr[x][y] = arr[tx][ty]
    arr[x1][y1 + 1] = flag
    return mini


def solution(rows, columns, queries):
    board = [[i + j for j in range(1, columns + 1)] for i in range(0, rows*columns, columns)]
    ans = []

    for query in queries:
        ans.append(turn(query, board))

    return ans


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
