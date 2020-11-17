import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

for _ in range(int(read())):
    n, idx = map(int, read().split())
    docs = list(map(int, read().split()))
    docs = deque(enumerate(docs))

    cnt = 0
    while docs:
        cur_max = max([x[1] for x in docs])
        if docs[0][1] == cur_max:
            cnt += 1
            if docs[0][0] == idx:
                print(cnt)
                break
            else:
                docs.popleft()

        else:
            docs.rotate(-1)
