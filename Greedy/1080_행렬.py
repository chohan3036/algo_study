def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]


def check_equality():
    for i in range(N):
        for j in range(M):
            if a[i][j] != b[i][j]:
                return 0
    return 1


N, M = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(N)]
b = [list(map(int, list(input()))) for _ in range(N)]

cnt = 0
for i in range(0, N - 2):
    for j in range(0, M - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1

if check_equality():
    print(cnt)
else:
    print(-1)
