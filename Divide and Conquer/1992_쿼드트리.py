import sys

def dv_cq(p, n):
    if p.count(0) == n*n:
        print(0, end='')
        return
    elif p.count(1) == n*n:
        print(1, end='')
        return

    temp = []
    for i in range(4):
        if i == 0:
            print('(', end='')
        for j in range(n//2):
            if i == 0:
                m = j*n
                c = p[m:m + n // 2]
                temp.extend(c)
            elif i == 1:
                m = j*n + n//2
                c = p[m:m + n // 2]
                temp.extend(c)
            elif i == 2:
                m = (j + n//2)*n
                c = p[m:m + n // 2]
                temp.extend(c)
            else:
                m = (j + n//2)*n + n//2
                c = p[m:m + n // 2]
                temp.extend(c)
        dv_cq(temp, n//2)
        temp.clear()
    print(')', end='')

N = int(sys.stdin.readline())
pic = []
for i in range(N):
    str = sys.stdin.readline()
    for j in range(N):
        pic.append(int(str[j]))

dv_cq(pic, N)