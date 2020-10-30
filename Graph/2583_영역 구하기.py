import sys
readline = lambda: sys.stdin.readline().strip()


def bfs(i, j):
    global visited, paper

    if paper[i][j] == 1:
        visited.append([i, j])
        return

    block = []
    queue = [[i, j]]

    while queue:
        [i, j] = queue.pop(0)
        block.append([i, j])
        visited.append([i, j])

        if paper[i][j] == 0:
            if i < M - 1 and paper[i + 1][j] == 0 and [i + 1, j] not in block and [i + 1, j] not in queue:
                queue.append([i + 1, j])
            if j < N - 1 and paper[i][j + 1] == 0 and [i, j + 1] not in block and [i, j + 1] not in queue:
                queue.append([i, j + 1])
            if i > 0 and paper[i - 1][j] == 0 and [i - 1, j] not in block and [i - 1, j] not in queue:
                queue.append([i - 1, j])
            if j > 0 and paper[i][j - 1] == 0 and [i, j - 1] not in block and [i, j - 1] not in queue:
                queue.append([i, j - 1])

    return len(block)


M, N, K = map(int, readline().split())
paper = [[0 for _ in range(N)] for _ in range(M)]

# 사각형 부분을 1로 만듦
for _ in range(K):
    x1, y1, x2, y2 = map(int, readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

visited = []
block_list = []

for i in range(M):
    for j in range(N):
        if [i, j] not in visited:
            block = bfs(i, j)
            if block:
                block_list.append(block)

print(len(block_list))
for i in sorted(block_list):
    print(i, end=' ')
