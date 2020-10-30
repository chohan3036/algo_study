import sys

readline = lambda: sys.stdin.readline().strip()

n = int(readline())
matrix = [list(map(int, list(readline()))) for _ in range(n)]

# 상하좌우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    size_list = []
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 or check[i][j]:
                continue
            else:
                queue = [(i, j)]
                check[i][j] = 1
                h_size = 1
                while queue:
                    cur = queue.pop()
                    for k in range(4):
                        nx = cur[0] + dx[k]
                        ny = cur[1] + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        elif matrix[nx][ny] and check[nx][ny] == 0:
                            check[nx][ny] = 1
                            queue = [(nx, ny)] + queue
                            h_size += 1
                size_list.append(h_size)

    return sorted(size_list)


result = bfs()
print(len(result))
for h in result:
    print(h)