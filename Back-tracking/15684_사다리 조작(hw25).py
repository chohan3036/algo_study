# 사다리 검사
# 시작한 번호가 사다리를 내려간 후에 그대로 나와야 함!


def check():
    for i in range(n):
        # 시작한 번호
        k = i
        for j in range(h):
            # 오른쪽 사다리 +1
            if ladder[j][k]:
                k += 1
            # 왼쪽 사다리 -1
            elif k > 0 and ladder[j][k - 1]:
                k -= 1
        if i != k:
            return False
    return True


def dfs(cnt, x, y):
    global ans

    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return

    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n - 1):
            if ladder[i][j]:
                j += 1
            else:
                ladder[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                ladder[i][j] = 0


n, m, h = map(int, input().split())
ladder = [[0] * (n) for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = 1

ans = 4