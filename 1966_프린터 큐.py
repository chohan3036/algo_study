import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

for _ in range(int(read())):
    n, idx = map(int, read().split())
    docs = list(map(int, read().split()))
    docs = list(enumerate(docs))

    queue = deque(docs)
    stack = [queue.popleft()]
    while queue:
        if stack[-1][1] < queue[0][1]:
            queue.extend(stack)
            stack.clear()
        stack.append(queue.popleft())

    for i in range(n):
        if stack[i][0] == idx:
            print(i + 1)
