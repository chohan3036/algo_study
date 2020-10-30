import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()


def bfs(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()

        if now == k:
            return arr[now][0]

        for next in (now + 1, now - 1, 2 * now):
            if LIMIT > next >= 0 == arr[next][0]:
                arr[next][0] = arr[now][0] + 1
                arr[next][1] = now
                q.append(next)


N, K = map(int, read().split())
LIMIT = 100001
time = [[0] * 2 for _ in range(LIMIT)]

print(bfs(time, N, K))

ways = deque()
time[N][1] = -1
now = K
while time[now][1] != -1:
    prev = time[now][1]
    ways.appendleft(prev)
    now = prev
print(' '.join(map(str, ways)), K)
