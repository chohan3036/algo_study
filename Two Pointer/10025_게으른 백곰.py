import sys
read = lambda: sys.stdin.readline().strip()

max_lo = 10**6
n, k = map(int, read().split())
board = [0 for _ in range(max_lo + 1)]
for _ in range(n):
    ice, lc = map(int, read().split())
    board[lc] = ice

if max_lo <= k:
    print(sum(board))

else:
    wsum, ans = 0, 0
    for end in range(max_lo):
        wsum += board[end]

        if end >= 2 * k:
            ans = max(ans, wsum)
            wsum -= board[end - 2 * k]

    print(ans)
