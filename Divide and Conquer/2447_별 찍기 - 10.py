# 재귀예요,, 재귀 맞지?
N = int(input())
mat = [[0 for _ in range(N)] for _ in range(N)]

def print_star(a, b, n):
    if n == 1:
        mat[a][b] = 1
        return

    nn = n//3
    for i in range(3):
        for j in range(3):
            na = a + nn*i
            nb = b + nn*j
            if i != 1 or j != 1:
                print_star(na, nb, nn)

print_star(0, 0, N)

for i in range(N):
    for j in range(N):
        if mat[i][j]:
            print('*', end='')
        else:
            print(' ', end='')
    print()