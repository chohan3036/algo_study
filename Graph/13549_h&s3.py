import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()


def bfs(arr, n, k):
    q = deque()
    q.append(n)
    arr[n] = 0

    while q:
        now = q.popleft()

        if now > k + 1:
            continue

        if now == k:
            return arr[now]

        for next in (2 * now, now + 1, now - 1):
            if LIMIT > next >= 0 and (arr[next] == -1 or arr[next] > arr[now]):
                if next == 2 * now:
                    arr[next] = arr[now]
                    q.appendleft(next)
                else:
                    arr[next] = arr[now] + 1
                    q.append(next)


N, K = map(int, read().split())
LIMIT = 100
time = [-1] * LIMIT

print(bfs(time, N, K))
