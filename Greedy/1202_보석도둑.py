import sys
from queue import PriorityQueue

N, K = map(int,sys.stdin.readline().split(' '))
A = []
for i in range(N):
    m, v = (map(int, sys.stdin.readline().split(' ')))
    A.append((m, v))
for i in range(K):
    A.append(((int(sys.stdin.readline())),2000000))
A.sort()

pq = PriorityQueue()
value = 0
for x in A:
    if x[1] != 2000000:
        pq.put(-x[1])
    else:
        if not pq.empty():
            value += pq.get()

print(-value)