import sys
read = lambda: sys.stdin.readline().strip()
import heapq as hq

for _ in range(int(read())):
    n, idx = map(int, read().split())
    docs = list(map(int, read().split()))

    q = []
    for x, y in enumerate(docs):
        hq.heappush(q, (-y, x))

