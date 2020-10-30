import sys
from collections import deque
read = lambda: sys.stdin.readline().strip()

# set prime table
prime = [1] * 10001
for i in range(2, 5000):
    if prime[i]:
        for j in range(i + i, 10001, i):
            prime[j] = 0


def bfs():
    queue = deque([(first, 0)])
    while queue:
        now, step = queue.popleft()
        if now == last:
            return step

        NOW = str(now)
        step += 1
        for i in range(4):
            for j in map(str, range(10)):
                if i == 0 and j == '0':
                    continue
                num = int(NOW[:i] + j + NOW[i + 1:])
                if prime[num] and not visited[num]:
                    visited[num] = 1
                    queue.append((num, step))


T = int(read())
for _ in range(T):
    first, last = map(int, read().split())
    visited = [0] * 10001
    print(bfs())
