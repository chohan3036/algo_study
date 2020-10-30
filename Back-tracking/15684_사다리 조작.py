import sys
read = lambda: sys.stdin.readline().strip()

N, M, H = map(int, read().split())
ver = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, read().split())
    ver[a - 1][b - 1] = 1
ans = 4


# 사다리 검사
def ladder():
    for i in range(N):
        k = i
        for j in range(H):
            if ver[j][k]:
                k += 1
            elif k > 0 and ver[j][k - 1]:
                k -= 1
        if i != k:
            return False
    return True


def dfs(cnt, x, y):
    global ans

    if ans <= cnt:
        return
    if ladder():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return

    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N - 1):
            if ver[i][j]:
                j += 1
            else:
                ver[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                ver[i][j] = 0


dfs(0, 0, 0)
print(ans if ans < 4 else -1)
