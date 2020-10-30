import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

N, M = map(int, read().split())
q = deque(i for i in range(1, N + 1))

idx = map(int, read().split())
cnt = 0

for x in idx:
    if q[0] != x:
        idx_q = q.index(x)
        gap = N - idx_q
        if idx_q <= N // 2:
            q.rotate(-idx_q)
            cnt += idx_q
        else:
            q.rotate(gap)
            cnt += gap
    q.popleft()
    N -= 1

print(cnt)
