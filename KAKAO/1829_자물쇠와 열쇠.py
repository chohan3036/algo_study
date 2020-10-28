from copy import deepcopy


# 90도 돌리기
def rotate(n, mat):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = mat[i][j]
    return result


def check(r, c, n, m, expanded_lock, key):
    cur_lock = deepcopy(expanded_lock)
    # 그냥 열쇠 끼우고 자물쇠 검사하자
    for i in range(r, r + n):
        for j in range(c, c + n):
            cur_lock[i][j] += key[i - r][j - c]
            if cur_lock[i][j] != 1:
                return False

    ## 자물쇠 검사하는 코드
    return True


def solution(key, lock):
    # 자물쇠와 열쇠 길이가 다를 수 있음....하
    n, m = len(key[0]), len(lock[0])
    expanded_len = (n - 1) * 2 + m

    # 자물쇠 배열을 padding 해줌(완탐 하기 쉽게)
    # 열쇠 크기만큼만 늘려주면 됨
    expanded_lock = [[0] * expanded_len for _ in range(expanded_len)]
    for i in range(m):
        for j in range(m):
            # 가운데에 자물쇠를 위치함
            expanded_lock[i + m - 1][j + m - 1] = lock[i][j]

    for _ in range(4):
        for i in range(expanded_len - m + 1):
            for j in range(expanded_len - m + 1):
                if check(i, j, n, m, expanded_lock, key):
                    return True
        key = rotate(n, key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[0, 1, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 0, 0]]))
