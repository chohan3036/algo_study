import sys

def quad_tree(x, y, t):
    global white, blue, mat
    color = mat[y][x]
    double_check = False

    for i in range(x, x+t):
        if double_check:
            break

        for j in range(y, y+t):
            if mat[j][i] != color:
                quad_tree(x, y, t//2)
                quad_tree(x + t//2, y, t//2)
                quad_tree(x, y + t//2, t//2)
                quad_tree(x + t//2, y + t//2, t//2)
                double_check = True
                break

    if not double_check:
        if mat[y][x] == 1:
            blue += 1
        else:
            white += 1

n= int(sys.stdin.readline())
mat = []
blue = 0
white = 0
for i in range(n):
    mat.append(list(map(int,input().split())))

quad_tree(0, 0, n)
print(white)
print(blue)
