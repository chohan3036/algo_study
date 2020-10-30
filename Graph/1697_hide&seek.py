import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()


def bfs(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()

        if now == k:
            return arr[now]

        for next in (now + 1, now - 1, 2 * now):
            if LIMIT > next >= 0 == arr[next]:
                arr[next] = arr[now] + 1
                q.append(next)


N, K = map(int, read().split())
LIMIT = 100001
time = [0] * LIMIT

print(bfs(time, N, K))
