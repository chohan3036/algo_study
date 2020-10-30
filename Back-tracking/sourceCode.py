"""
14889 - 스타트와 링크

# first와 second는 빈 리스트로 시작
def go(index, first, second):
    # 탈출 조건 : 주어진 n명 모두 분배했으면
    if index == n:
        # 반씩 분배 안 됐으면 -1 반환
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff

    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1

    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(go(0, [], []))


# 2529 - 부등호
def ok(num):
    for i in range(n):
        if a[i] == '<':
            if num[i] > num[i+1]:
                return False
        elif a[i] == '>':
            if num[i] < num[i+1]:
                return False
    return True

def go(index, num):
    if index == n+1:
        if ok(num):
            ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        check[i] = True
        go(index+1, num+str(i))
        check[i] = False

n = int(input())
a = input().split()
ans = []
check = [False] * 10
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])



# 1248 - 맞춰봐
def ok():
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += ans[j]
            if sign[i][j] == 0:
                if s != 0:
                    return False
            elif sign[i][j] > 0:
                if s <= 0:
                    return False
            elif sign[i][j] < 0:
                if s >= 0:
                    return False
    return True

def go(index):
    if index == n:
        return ok()
    for i in range(-10, 11):
        ans[index] = i
        if go(index+1):
            return True
    return False

n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(' '.join(map(str,ans)))



# 맞춰봐 - 1248 개선버전
def check(index):
    s = 0
    for i in range(index,-1,-1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

def go(index):
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and go(index+1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and go(index+1):
            return True
    return False

n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(' '.join(map(str,ans)))



# n queen - 9663
def check(row, col):
    for i in range(n):
        if i == row:
            continue
        if a[i][col]:
            return False
    x = row-1
    y = col-1
    while x >= 0 and y >= 0:
        if a[x][y]:
            return False
        x -= 1
        y -= 1
    x = row-1
    y = col+1
    while x >= 0 and y < n:
        if a[x][y]:
            return False
        x -= 1
        y += 1
    return True

def calc(row):
    if row == n:
        global ans
        ans += 1
        return
    for col in range(n):
        a[row][col] = True
        if check(row, col):
            calc(row+1)
        a[row][col] = False


n = int(input())
ans = 0
a = [[False]*n for _ in range(n)]
calc(0)
print(ans)



# n queen -
def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True

def calc(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row,col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans

n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)
print(calc(0))


# 스도쿠 - 2580
def square(x, y):
    return (x//3)*3+(y//3)

def go(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str,row)))
        return True
    x = z//n
    y = z%n
    if a[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[square(x,y)][i] == False:
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                a[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = False
    return False
n = 9
a = [list(map(int,input().split())) for _ in range(n)]
c = [[False]*10 for _ in range(n)]
c2 = [[False]*10 for _ in range(n)]
c3 = [[False]*10 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c[i][a[i][j]] = True
            c2[j][a[i][j]] = True
            c3[square(i,j)][a[i][j]] = True
go(0)


# 알파벳 - 1987
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def go(board, check, x, y):
    n = len(board)
    m = len(board[0])
    ans = 0
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            ch = ord(board[nx][ny])-ord('A')
            if check[ch] == False:
                check[ch] = True
                temp = go(board, check, nx, ny)
                if ans < temp:
                    ans = temp
                check[ch] = False
    return ans+1

n,m = map(int,input().split())
board = [input() for _ in range(n)]
check = [False]*26
check[ord(board[0][0])-ord('A')] = True
print(go(board,check,0,0))

"""