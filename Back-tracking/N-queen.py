def dfs(n, y, col, diag1, diag2):
    global ans

    if y == n:
        ans += 1
        return

    for x in range(n):
        if x in col or (x + y) in diag1 or (x - y) in diag2:
            continue
        col.add(x)
        diag1.add(x + y)
        diag2.add(x - y)
        dfs(n, y + 1, col, diag1, diag2)
        col.remove(x)
        diag1.remove(x + y)
        diag2.remove(x - y)


n = int(input())
ans = 0

col, diag1, diag2 = set(), set(), set()
dfs(n, 0, col, diag1, diag2)

print(ans)
