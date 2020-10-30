import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()


def bfs(arr, n, k):
    q = deque()
    q.append(n)
    ans, cnt = 0, 0

    while q:
        now = q.popleft()

        if now == k:
            ans = arr[now]
            cnt += 1
            if ans == 0:
                return ans, cnt

        for next in (now + 1, now - 1, 2 * now):
            if not LIMIT > next >= 0:
                continue
            if arr[next] == 0 or arr[next] == arr[now] + 1:
                arr[next] = arr[now] + 1
                q.append(next)

    return ans, cnt


N, K = map(int, read().split())
LIMIT = 100001
time = [0] * LIMIT

for x in (bfs(time, N, K)):
    print(x)
