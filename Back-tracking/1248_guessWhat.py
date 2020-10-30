import sys
read = lambda: sys.stdin.readline().strip()


def ok(idx):
    sign = 0
    for i in range(idx, -1, -1):
        sign += num[i]
        if s[i][idx] > 0:
            if not sign > 0:
                return False
        elif s[i][idx] < 0:
            if not sign < 0:
                return False
        else:
            if sign != 0:
                return False
    return True


def go(idx):
    if idx == n:
        return True
    # i = j인 s 배열 원소는 해당 idx 숫자의 부호를 의미함
    # 예) s[0][0]은 0번째부터 0번째까지 수열의 합

    # 부호가 0이면 0임
    if s[idx][idx] == 0:
        num[idx] = 0
        return ok(idx) and go(idx + 1)

    # 부호에 따라 음수, 양수 배정함
    for i in range(1, 11):     # 그럼 20개 안하고 10개만 해도 됨
        num[idx] = s[idx][idx] * i
        if ok(idx) and go(idx + 1):
            return True
    return False


n = int(read())
num = [0 for _ in range(n)]

str_list = list(read())
s = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i, n):
        if str_list[cnt] == '+':
            s[i][j] = 1
        elif str_list[cnt] == '-':
            s[i][j] = -1
        else:
            s[i][j] = 0
        cnt += 1
print(s)
''' 이 모양의 s 행렬 만들기
  0 1 2 3
0 0 0 0 0
1 - 0 0 0
2 - - 0 0
3 - - - 0
'''

go(0)
print(' '.join(map(str, num)))
